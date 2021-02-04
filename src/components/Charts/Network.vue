<template>
  <div class="network">
    <div class="container-body">
    <div class="body-text">
      <p>Spodaj lahko raziskuješ Twitter prostor, ki ga ustvarja več kot 6000 uporabniških računov. Ti pripadajo tako resničnim ljudem, kot neavtentičnim manipulatorjem. Nastavljaš lahko razmerje med originalnimi tviti in ritviti ter datum registracije. Skupine uporabnikov, ki so si sorodne, so obarvane z isto barve in se nahajajo bližje v prostoru. Več informacij o skupini dobiš s klikom na njenega pripadnika.</p>
      <p>Omrežje je sestavljeno na podlagi strojne analize tvitov posameznih uporabnikov. Za vsakega uporabnika izračunamo število omemb domen, drugih uporabnikov, ključnikov in posameznih besed (če so se te omembe v celotnem korpusu pojavile več kot petkrat). Dobimo matriko, kjer vsakega uporabnika opisuje nekaj več kot 2600 parametrov (številk). Slednje z algoritmom UMAP (z evklidsko inicializacijo) pretvorimo v koordinate v dvodimenzionalnem prostoru. Ko imamo koordinate vseh uporabnikov, jih z algoritmom HDBSCAN ločimo v kategorije, ki so obarvane na grafu.</p>
      <p>Ob kliku na kategorijo se pod omrežjem izpišejo najpogostejše omembe, domene in ključniki za izbrano kategorijo.</p>
      <p><b>Opozorilo:</b> kategorij je več kot 200, razločljivih barv pa občutno manj. V isto kategorijo na vizualizaciji spadajo uporabniki, ki so iste barve in so si blizu v koordinatnem prostoru.</p>
      <p>Večji, kot je krog, več tvitov je uporabnik_ca sproduciral_a (kvadratni koren števila tvitov).</p>
      <p>Eksperimentalna kategorizacija med "levo" in "desno" temelji na ročno definiranem naboru "zagotovo levičarskih" in "zagotovo desničarskih" uporabniških računov, na podlagi katerega se trenira prediktivni model. Trening zaključimo, ko model postane več kot 81 % (kar seveda ni dovolj) "zanesljiv".</p>
    </div>
    </div>
    <div class="controls-container">
      <div class="left-hand-container lhc-50">
        <div class="slider-container">
          <h1 class="title">Razmerje med originalnimi in poobjavljenimi tviti: <b>{{ rt_threshold.toString().replace('.', ',') }}</b>.</h1>
          <vue-slider
            :v-data="rtThresholds"
            @change="val => rt_threshold = val / 4"
            @drag-end="refreshGraph()"
            :dot-size="20"
            tooltip="none"
          />
        </div>
      </div>
      <div class="right-hand-container rhc-50">
        <div class="slider-container">
          <h1 class="title" style="min-height: 86px">Registrirani leta <b>{{ registrationYear }}</b> ali kasneje.<br/></h1>
          <vue-slider
            :marks="[2006, 2014, 2021]"
            :v-data="years"
            v-model="registrationYear"
            @drag-end="setRegistrationThreshold(registrationYear)"
            :dot-size="20"
            tooltip="none"
          />
        </div>
      </div>
    </div>
    <div class="controls-container">
      <div class="left-hand-container">
        <div id="graph"></div>
      </div>
      <div class="right-hand-container table-container">
        <table class="header-table">
          <thead>
            <tr>
              <th scope="col" style="text-align: left; width: 10rem;">
                Profil
              </th>
              <th scope="col" style="text-align: left; width: 10rem;">
                Registracija
              </th>
              <th scope="col" style="text-align: left; width: 10rem;">
                RT razmerje
              </th>
            </tr>
          </thead>
        </table>
        <div class="body-table-container">
          <table class="body-table">
            <tbody>
              <tr v-for="user in cluster_users" :key="user.id">
                <td><a :href="`https://twitter.com/${user.label}`" target="_blank">{{user.label}}</a></td>
                <td>{{ new Date(user.date).toLocaleDateString('sl')}}</td>
                <td>{{ user.rt ? (user.rt + "").slice(0, 5) : '???' }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="controls-container">
        <button @click="toggle_graph()">
          {{ graph_type ? 'Izklopi' : 'Vklopi' }} eksperimentalni prikaz "levih"/"desnih"
        </button>
    </div>
    <div class="controls-container">
        <div class="body-text" v-if="graph_type">
          Bolj ko so uporabniki modre barve, bolj so "levičarji", bolj ko so rdeče barve bolj so "desničarji". Če so črne barve najverjetneje ne govorijo slovensko ali jih kako drugače nismo znali klasificirati.
        </div>
        <!-- <p style="text-align: center; background: rgba(255, 0, 0, 0.3); padding: 10px;">
          Klikni na obarvano skupino vomrežju da vidiš njene člane.
        </p> -->
    </div>
    <div id="charts">
      <div class="chart-container">
        <network-bar-chart :data="group_urls" :id="'urls'" :color="currentColor" datasetName="Top domene" />
      </div>
      <div class="chart-container">
        <network-bar-chart :data="group_hashtags" :id="'hashtags'" :color="currentColor" datasetName="Top ključniki" />
      </div>
      <div class="chart-container">
        <network-bar-chart :data="group_rts" :id="'rts'" :color="currentColor" datasetName="Top ritviti" />
      </div>
    </div>
    <div class="col-8 sptop" id="dists">
      <div id="tooltip"></div>
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import Sigma from 'sigma';
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'

import NetworkBarChart from './NetworkBarChart.vue';

export default {
  name: 'Network',
  components: { NetworkBarChart, VueSlider },
  data() {
      return {
        rtThresholds: {
          0: '0',
          1: '1/4',
          2: '1/2',
          3: '3/4',
          4: '1'
        },
        years: [
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
        ],
        registrationYear: 2000,
        currentColor: '#ffffff',
        lr: {left: 0, right: 0, other:0},
        cluster_users: [],
        graph: {},
        cs: d3.scaleLinear().range(["#fd8d3c", "#b10026"]).domain([0.5, 1]),
        csa: d3.scaleLinear().range(["#41b6c4", "#253494"]).domain([0.5, 1]),
        cs2: d3.scaleOrdinal(d3.schemePaired),//d3.interpolateWarm, //d3.scaleOrdinal().range(d3.interpolateSpectral),//d3.schemeSet3),
        date_threshold_date: 0,
        date_threshold: '',
        graph_type: true,
        rt_threshold: 0,
        group_hashtags: [],
        group_rts: [],
        group_urls: [],
        horizontal_options: {
            chart: {
                type: 'multiBarHorizontalChart',
                height: 280,
                margin : {
                    top: 20,
                    right: 20,
                    bottom: 45,
                    left: 100
                },
                showControls: false,
                x: function(d){return d.label;},
                y: function(d){return d.value;},

                showValues: true,
                duration: 500,
                xAxis: {
                    showMaxMin: false
                },
                yAxis: {
                    axisLabel: 'Pogostost',
                    tickFormat: function(d){
                        return d3.format(',.2f')(d);
                    }
                }
            }
        },
      };
  },
  mounted() {
    // app.controller('MainCtrl', function(this, $http, $q) {
    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    this.monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
    let tooltip = d3.select("#tooltip")

    this.load_graph()
  },
  methods: {
    refreshGraph() {
      console.log(this.rt_threshold);
        this.sigma.graph.nodes()
            .forEach(d => {
                if (d.v[0] < this.rt_threshold) d.hidden = true
                else if (d.date < this.date_threshold_date) d.hidden = true
                else d.hidden = false
            })
        this.sigma.refresh();
        this.cluster_users = this.sigma.graph.nodes()
            .filter(d => d.cluster === this.cluster)
            // .filter(d => {
            //     console.log(this.date_threshold_date, d.date);
            //     return d.date > this.date_threshold_date
            // })
            .filter(d => d.date > this.date_threshold_date)
            .filter(d => d.v[0] > this.rt_threshold)
        this.lr.left = this.sigma.graph.nodes()
            .filter(d => d.date > this.date_threshold_date)
            .filter(d => d.v[0] > this.rt_threshold)
            .filter(d => d.lefty).length
        this.lr.right = this.sigma.graph.nodes()
            .filter(d => d.date > this.date_threshold_date)
            .filter(d => d.v[0] > this.rt_threshold)
            .filter(d => d.troll).length
    },
    setRegistrationThreshold(year) {
        this.date_threshold_date = new Date(`${year}-01-01`);
        console.log(this.graph.nodes[0].date < this.date_threshold_date);
        console.log(this.date_threshold_date);
        this.refreshGraph();
    },
    setRtThreshold(newThreshold) {
        this.rt_threshold = newThreshold;
        console.log(rt_threshold);
        this.refreshGraph();
    },
    goToTwitter(e) {
        window.open("https://twitter.com/" + e.data.node.label, "_blank")
    },
    async load_graph() {
        const response = await fetch('data/user_network.json');
        const r1 = await response.json();
        this.graph = r1;
        let mindate = 1000000000000000;
        let maxdate = 0;
        this.graph.nodes
            .forEach(d => {
                d.oldColor = d.color;
                d.date = new Date(d.date)
                if (d.date < mindate) mindate = d.date.getTime();
                if (d.date > maxdate) maxdate = d.date.getTime();
                if (d.troll) {
                    d.color = this.cs(d.troll_prob)
                }
                else if (d.lefty) {
                    d.color =this.csa(d.left_prob)
                    //console.log(">", d.amp_prob)
                }
                else d.color = "#000000"
                if (d.troll) this.lr.right += 1
                if (d.lefty) this.lr.left += 1
            })

        this.sigma = new Sigma(
            {
                renderer: {
                    container: document.getElementById("graph"),
                    type:"webgl"
                },
                settings: {
                    edgeColor: "default",
                    defaultNodeColor: "steelblue",
                    defaultLabelColor: '#666',
                    defaultEdgeColor: "#aaa",
                    labelSize : 'proportional',
                    labelSizeRatio : 1.5,
                    labelThreshold : 5.5,
                    drawEdges : false,
                    minNodeSize : 1,
                    maxNodeSize : 8,
                    minEdgeSize : 0.15,
                    maxEdgeSize : 1,
                    zoomMin : .001,
                    zoomMax : 3,
                    font : "Arial",
                    batchEdgesDrawing:true,
                    // webglEdgesBatchSize:100,
                    hideEdgesOnMove:true,
                    zoomingRatio: 2.3,
                    scalingMode: "outside"
                },
                graph: this.graph,
            }
        );
        this.sigma.bind('clickNode', (e) => {
            this.goToTwitter(e)
        })

        this.toggle_graph();
    },
    async load_group(n) {
        const response = await fetch(`data/group_${n}.json`)
        const r1 = await response.json()
        // const r1 = await fetch(`data/group_${n}.json`).then(response => response.json());
        // let r1 = $http.get("data/group_" + n + ".json");
        let group = r1;
        this.group_hashtags = [{key: "top hashtags", values: group.hashtags}];
        this.group_urls = [{key: "top URLS", values: group.urls}];
        this.group_rts = [{key: "top retweeted", values: group.retweets}];
        this.currentColor = this.cs2((n + 1) / 241);
        // this.currentColor = '#ffffff';
        console.log('LALALA');
        console.log((n+1)/241);
        console.log(this.currentColor);
    },
    toggle_graph() {
        this.graph_type =  !this.graph_type;
        //console.log(this.sigma.graph.nodes())
        if (this.graph_type === false) {

            this.sigma.graph.nodes()
                .forEach(d => {
                    d.oldColor = d.color;
                    if (d.cluster === -1) d.color = "#999999";
                    else  d.color = this.cs2((d.cluster + 1) / 241)
                })
            this.sigma.refresh()
            this.sigma.unbind('clickNode')
            this.sigma.bind('clickNode', (e) => {
                this.cluster = e.data.node.cluster
                this.load_group(e.data.node.cluster)
                console.log(this.cluster);
                const test = this.sigma.graph.nodes()
                    .filter(d => d.cluster === this.cluster)
                console.log(test);
                this.cluster_users = this.sigma.graph.nodes()
                    .filter(d => d.cluster === this.cluster)
                    .sort((a, b) => {return b.v[0] - a.v[0]})
                    .map(node => {
                        node.rt = node.v[0];
                        node.v = '';
                        return node;
                    });
                // console.log(this.cluster_users);
            })
        }
        else {
            this.sigma.graph.nodes()
                .forEach(d => {
                    d.color = d.oldColor;
                })
            // this.sigma.unbind('clickNode')
            this.sigma.refresh()
            // this.sigma.bind('clickNode', this.goToTwitter)
        }
        this.sigma.refresh()
    }
  },
};
</script>

<style>
.container-body {
  display: flex; /* or inline-flex */
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 68px;
}
#charts {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.chart-container {
  width: 33%;
}
.title {
      /* Style for "Prostorski" */
  color: #000000;
  font-family: "buran_ussrregular";
  font-weight: 400;
  font-style: normal;
  letter-spacing: normal;
  text-align: center;
  letter-spacing: 2.3px;
  line-height: normal;
  margin-left: 10px;
  margin-right: 10px;
  cursor: pointer;
  text-align: left;
}
.controls-container {
  width: 100%;
  display: flex;
  flex-wrap: nowrap;
}
.slider-container {
  padding: 40px;
}
.left-hand-container {
  width: 65%;
}
.right-hand-container {
  width: 35%;
}

.full {
    width: 100%;
}
.network {
    width: 100%;
}
#graph {
    width: calc(100% - 4px);
    height: 700px;
    position: relative;
    overflow: hidden;
    float: left;
    border: 2px solid #000000;
}
#graph canvas {
    left: 0;
    z-index: 1;
}

.body-text {
    /* Style for "Lorem ipsu" */
    color: #000000;
    font-family: acumin-pro, sans-serif;
    font-size: 20px;
    font-weight: 300;
    font-style: normal;
    letter-spacing: normal;
    line-height: 33.33px;
    text-align: left;
    /* Text style for "Lorem ipsu" */
    font-style: normal;
    letter-spacing: normal;
    margin: 0 auto;
    width: 90vw;
    max-width: 100%;
  }

@media only screen and (min-width: 769px) {
  .body-text {
		width: 50vw;
  }
}

.users {
    width: 100%;
}

.table-container {
    max-height: 700px;
    text-align: left;
    float: left;
    padding: 0;
    border: 2px solid #000000;
    border-left: none;
    position: relative;
    overflow: hidden;
}
table {
  position: relative;
  width: 100%;
  table-layout: fixed;
  font-family: acumin-pro, sans-serif;
}
table a {
  color: #000000;
  font-weight: bold;
  padding-left: 4px;
}
.table-container td:nth-child(2),
.table-container td:nth-child(3) {
  text-align: right;
  padding-right: 10px;
}
.header-table {
  background-color: #ffffff;
  border-bottom: 2px solid #000000;
}
.body-table-container {
  overflow-y: auto;
  height: 100%;
}
.body-table {
  padding-bottom: 5px;
}

.lhc-50, .rhc-50 {
  width: 50%;
  max-width: 50%;
}

/* slider */
.vue-slider-mark-label, button {
  color: #000000;
  font-family: "buran_ussrregular";
  font-weight: 400;
  font-style: normal;
  letter-spacing: normal;
  text-align: center;
  letter-spacing: 2.3px;
  line-height: normal;
  margin-left: 10px;
  margin-right: 10px;
  cursor: pointer;
  text-align: left;
  font-size: 16px;
}

button {
  height: 60px;
  border-radius: 0;
  border: 2px solid #000000;
  box-shadow: none;
  display: block;
  margin: auto;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-left: 30px;
  padding-right: 30px;
  background-color: #f9e96f;
}

.vue-slider-rail,
.vue-slider:hover .vue-slider-rail {
  background-color: #000000;
}
.vue-slider-process,
.vue-slider:hover .vue-slider-process {
  background-color: #f9e96f;
}
.vue-slider-mark-step {
  box-shadow: 0 0 0 2px #000000;
}
.vue-slider-mark-step-active,
.vue-slider:hover .vue-slider-mark-step-active {
  /* border-color: #000000; */
  box-shadow: 0 0 0 2px #000000;
}
.vue-slider-dot-handle,
.vue-slider-dot-handle:hover,
.vue-slider:hover .vue-slider-dot-handle {
  border-color: #000000;
}
.vue-slider-dot-handle-focus,
.vue-slider-process:hover .vue-slider-dot-handle-focus,
.vue-slider-dot-handle-focus:hover,
.vue-slider:hover .vue-slider-dot-handle:hover {
  border-color: #000000;
  box-shadow: 0 0 0 5px rgba(0, 0, 0, 0.2);
}


@media (max-width: 1200px) {
  .controls-container {
    flex-wrap: wrap;
  }
  .left-hand-container, .right-hand-container {
    width: 100%;
    max-width: 100%;
  }
  #graph {
    height: 400px;
  }
  .table-container {
    border-left: 2px solid #000000;
    height: 400px;
  }
  .chart-container {
    width: 100%;
  }
}

@media (max-width: 576px) {
  th:nth-child(3),
  td:nth-child(3) {
    display: none;
  }
}
</style>