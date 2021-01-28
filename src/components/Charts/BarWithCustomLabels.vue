<template>
  <div class="container">
    <div class="labels-container">
      <div @click="updateChart('control')" class="lables">
      <img alt="" src="/yellow.png"/>
        <span v-if="clickedLabel.control">
          <strike>Kontrolni vzorec</strike>
        </span>
        <span v-else>
          Kontrolni vzorec
        </span>
      </div>
      <div  @click="updateChart('brigade')" class="lables">
      <img alt="" src="/green.png"/>
        <span v-if="clickedLabel.brigade">
          <strike>Brigada</strike>
        </span>
        <span v-else>
          Brigada
        </span>
      </div>
      <div  @click="updateChart('fake')" class="lables">
      <img alt="" src="/red.png"/>
        <span v-if="clickedLabel.fake">
          <strike>Lažni profili</strike>
        </span>
        <span v-else>
          Lažni profili
        </span>
      </div>
      <div  @click="updateChart('politiki')" class="lables">
      <img alt="" src="/blue.png"/>
        <span v-if="clickedLabel.politiki">
          <strike>Politiki</strike>
        </span>
        <span v-else>
          Politiki
        </span>
      </div>
    </div>
    <div class="canvas">
      <canvas :id="id"></canvas>
    </div>
  </div>
</template>
<script>
import Chart from 'chart.js';
import configure from './barChartConfiguration.js'
import createSimpleData from './createChartDataSimple.js'

export default {
  name: "BarCustomLabels",
    props: {
      id: { type: String, required: true },
      data: { type: Object }, 
  },
    data () {
      return {
        myChart: {},
        activeDataset: [],
        inactiveDataset: [],
        clickedLabel: {
          fake: false,
          politiki: false,
          brigade: false,
          control: false,
        }
      }
    },
    methods: {
      createChart(chartId, chartData) {
        const ctx = document.getElementById(chartId);
        ctx.fillStyle = 'white';
        ctx.style.backgroundColor = 'white';
        this.$data.myChart = new Chart(ctx, {
          type: 'bar',
          data: chartData.data,
          options: {
            legend: {
              display: false
              },
            maintainAspectRatio: false,
            responsive: true,
            lineTension: 1,
            scales: {
              yAxes: [{
                ticks: {
                  beginAtZero: true,
                  padding: 25,
                  autoSkip: false,
                  fontSize: 18,
                  callback: function (tick) {
                    if (tick.length > 12) return tick.substring(0, 9)+"...";
                    else return tick
                }
                }
              }],
              xAxes: [{
                ticks: {
                  beginAtZero: true,
                }
              }]
            },
            events: ["mousemove", "mouseout", "click", "touchstart", "touchmove", "touchend"],
          }
        });
      },
			updateChart(id) {
        this.clickedLabel[id] = this.clickedLabel[id] ? false : true;
        let element = this.activeDataset.find((el) => el.id === id);
        if (element) {
          this.activeDataset = this.activeDataset.filter((el) => el.id !== id)
          this.inactiveDataset.push(element)
        } else {
          element = this.inactiveDataset.find((el) => el.id === id);
          this.inactiveDataset = this.inactiveDataset.filter((el) => el.id !== id)
          this.activeDataset.push(element)
        }
        this.$data.myChart.data.datasets =  this.activeDataset
        this.$data.myChart.update();
			},
  },
  mounted() {
    if (this.data) { 
      this.createChart(this.id, this.data);
      this.activeDataset = this.data.data.datasets;
      }
  },
};
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: column;
    margin: 5px auto;
  }
  .labels-container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin-left: 100px;
    margin-bottom: 20px;
  }
  .canvas {
    margin: 0 auto;
    width: 80vw;
    max-width: 1200px;
    min-width: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
    height: 50vh;
  }
  .lables {
    padding: 5px;
    margin: 5px;
    border: 1px solid black;
    border-radius: 25px;
    cursor: pointer;
  }
    img {
    /* Style for "Layer 32" */
			width: 15px;
			height: 15px;
			object-fit: cover;
  }
</style>