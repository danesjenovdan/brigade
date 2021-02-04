<template>
  <div class="network">
    <div class="col-3 sptop" id="graphctrl">
        <div class="row" style="width: 60%; float: left; text-align: left;">

            <div class="col-12 sptop nopad small" >
                <button @click="setRtThreshold(0)">Uporabniki ne glede na RT</button>
                <button @click="setRtThreshold(0.5)">Uporabniki, ki vsaj pol časa ritvitajo</button>
                <button @click="setRtThreshold(0.75)">Uporabniki, ki vsaj tri četrt časa ritvitajo</button>
            </div>
            <div class="col-12 sptop" id="rtslider"></div>
            <div class="col-12 sptop nopad small" >
                Registriran leta <b>{{ registrationYear }}</b> ali kasneje.
                <vue-slider :v-data="years" v-model="registrationYear" @drag-end="setRegistrationThreshold(registrationYear)" />
            </div>
            <div class="col-12 sptop" id="dateslider"></div>
        </div>
        <div class="row" style="width: 40%; float: left;">
            <div class="col-12 nopad">
                <button class="btn btn-sm btn-primary" @click="toggle_graph()" style="width: 60%; height: 60px; display: inline-block; border-radius: 0;">Klikni za experimentalni prikaz političnih osi</button>
                <div class="full" v-if="graph_type">
                    Barve: <span class="badge badge-primary" style="background-color:#4575b4;width:100px">Left wing {{lr.left}}</span>,
                    <span class="badge badge-primary" style="background-color:#d73027;width:150px">Right wing {{lr.right}}</span>,
                    <span class="badge badge-primary" style="background-color:#000000;width:100px">Others</span>,
                </div>
            </div>
        </div>
    </div>
    <div id="graph">
        <div id="graph-overlay"></div>
    </div>
    <div class="table-container">
        <p style="text-align: center; background: rgba(255, 0, 0, 0.3); padding: 10px;">Klikni na obarvano skupino v omrežju da vidiš njene člane.</p>
        <table>
            <thead>
            <tr>
                <th scope="col" style="text-align: left; width: 10rem;">
                Username
                </th>
                <th scope="col" style="text-align: left; width: 10rem;">
                Registration
                </th>
                <th scope="col" style="text-align: left; width: 10rem;">
                RT/OC
                </th>
                <th scope="col" style="text-align: left; width: 10rem;">
                Politična klasifikacija
                </th>
            </tr>
            </thead>
            <tbody>
                <tr v-for="user in cluster_users" :key="user.id">
                <td><a :href="`https://twitter.com/${user.label}`" target="_blank">{{user.label}}</a></td>
                <td>{{ new Date(user.date).toLocaleDateString('sl') }}</td>
                <td>{{ (user.rt + "").slice(0, 5) }}</td>
                <td>{{ user.lefty ? 'Morda "levičar"' : 'Morda "desničar"' }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="charts">
        <div class="chart-container">
            <network-bar-chart :data="group_hashtags" :id="'hashtags'" :color="currentColor" />
        </div>
        <div class="chart-container">
            <network-bar-chart :data="group_urls" :id="'urls'" :color="currentColor" />
        </div>
        <div class="chart-container">
            <network-bar-chart :data="group_rts" :id="'rts'" :color="currentColor" />
        </div>
    </div>
    <div class="col-8 sptop" id="dists">
    <div id="tooltip"></div>
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import * as noUiSlider from 'nouislider';
import * as sigma from 'sigma';
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'

import NetworkBarChart from './NetworkBarChart.vue';

export default {
  name: 'Network',
  components: { NetworkBarChart, VueSlider },
  data() {
      return {
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
    let rtslider = document.getElementById('rtslider');
    let dateslider = document.getElementById('dateslider');
    noUiSlider.create(rtslider, {
        start: [0],
        connect: true,
        range: {
            'min': 0.0,
            'max': 1.0
        }
    });

    this.load_graph()
  },
  methods: {
    refreshGraph() {
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

        noUiSlider.create(dateslider, {
            start: [mindate],
            connect: true,
            range: {
                'min': mindate,
                'max': maxdate
            }
        });

        this.sigma = new sigma(
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
        rtslider.noUiSlider.on('end', (values, handle) => {
            this.rt_threshold= values[handle];
            this.sigma.graph.nodes()
                .forEach(d => {
                    if (d.v[0] < values[handle]) d.hidden = true
                    else d.hidden = false
                })
            this.sigma.refresh();
            this.cluster_users = this.sigma.graph.nodes()
                .filter(d => d.cluster === this.cluster)
                .filter(d => d.date > this.date_threshold_date)
                .filter(d => d.v[0] > values[handle])
            this.lr.left = this.sigma.graph.nodes()
                .filter(d => d.date > this.date_threshold_date)
                .filter(d => d.v[0] > values[handle])
                .filter(d => d.lefty).length
            this.lr.right = this.sigma.graph.nodes()
                .filter(d => d.date > this.date_threshold_date)
                .filter(d => d.v[0] > values[handle])
                .filter(d => d.troll).length
            this.$apply()
        });
        dateslider.noUiSlider.on('end', (values, handle) => {
            this.date_threshold_date= new Date(Math.floor(values[handle]));
            //console.log(this.date_threshold)
            this.date_threshold = this.monthNames[this.date_threshold_date.getMonth()] + "-" + this.date_threshold_date.getFullYear()
            this.sigma.graph.nodes()
                .forEach(d => {
                    if (d.date < values[handle]) d.hidden = true
                    else d.hidden = false
                })
            this.sigma.refresh();
            this.cluster_users = this.sigma.graph.nodes()
                .filter(d => d.date > this.date_threshold_date)
                .filter(d => d.cluster === this.cluster)
                .filter(d => d.v[0] > this.rt_threshold)

            this.lr.left = this.sigma.graph.nodes()
                .filter(d => d.date > this.date_threshold_date)
                .filter(d => d.v[0] > this.rt_threshold)
                .filter(d => d.lefty).length
            this.lr.right = this.sigma.graph.nodes()
                .filter(d => d.date > this.date_threshold_date)
                .filter(d => d.v[0] > this.rt_threshold)
                .filter(d => d.troll).length
            this.$apply()
        });

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
.full {
    width: 100%;
}
.network {
    width: 100%;
}
#graph {
    width: 70%;
    height: 700px;
    position: relative;
    overflow: hidden;
    float: left;
}
#graph-overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    pointer-events: none;
    background: rgba(0, 0, 0, 0);
    z-index: 2;
    border: 2px solid #000000;
}
#graph canvas {
    left: 0;
    z-index: 1;
}

.chart-container {
    width: 33%;
    float: left;
}
.users {
    width: 100%;
}

.table-container {
    width: 25%;
    max-height: 700px;
    overflow-y: auto;
    text-align: left;
    float: left;
    padding-left: 20px;
}
</style>