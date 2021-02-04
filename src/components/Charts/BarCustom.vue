<template>
  <div class="container">
    <div class="labels-container">
      <slot></slot>
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
  name: "BarCustom",
    props: {
      id: { type: String, required: true },
      data: { type: Object },
			fillColor: { type: String },
			borderColor: { type: String },
      displayLabel: { default: true, type: Boolean }
  },
    data () {
      return {
        myChart: {}
      }
    },
    methods: {
      createChart(chartId, chartData) {
        const ctx = document.getElementById(chartId);
        ctx.fillStyle = 'white';
        ctx.style.backgroundColor = 'white';
        this.$data.myChart = new Chart(ctx, {
          type: chartData.type,
          data: chartData.data,
          options: chartData.options,
        });
				const myChart = this.$data.myChart
				document.getElementById(chartId).onclick = function(evt){
            const activePoints = myChart.getElementsAtEvent(evt);
            const firstPoint = activePoints[0];
            const label = myChart.data.labels[firstPoint._index];
            const value = myChart.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
            let url;
            switch(true) {
              case chartId.includes('hashtag'):
                url = 'https://twitter.com/hashtag/'+label.substring(label.lastIndexOf("#") + 1, label.length);
                break;
              case chartId.includes('mentions'):
                url = 'https://twitter.com/'+label
                break;
              case chartId.includes('retweets'):
                url = 'https://twitter.com/'+label
                break;
              case chartId.includes('domains'):
                // url = 'https://'+label
                url = `https://twitter.com/search?q=${label}`;
                break;
              default:
                // code block
            }
            if (firstPoint !== undefined)
            window.open(url, '_blank');
        };
      }
  },
  mounted() {
    if (this.data && this.data.data) {
			const configured = configure(this.data.data.labels,
			this.data.data.datasets[0].label,
			this.data.data.datasets[0].data,
			this.borderColor,
			this.fillColor,
			this.id,
      this.displayLabel
			)
      this.createChart(this.id, configured);
      }
  },
    watch: {
    data(newVal) {
      console.log(this.data);
      if (!this.$data.data && this.$data.data !== undefined)  {
        const configured = configure(this.data.data.labels,
        this.data.data.datasets[0].label,
        this.data.data.datasets[0].data,
        this.borderColor,
        this.fillColor,
        this.id,
        this.displayLabels
        )
        this.createChart(this.id, configured);
      } else {
        this.$data.myChart.data.labels = newVal.data.labels;
        this.$data.myChart.data.datasets = newVal.data.datasets
        this.$data.myChart.data.datasets[0].borderColor = this.borderColor;
        this.$data.myChart.data.datasets[0].backgroundColor = this.fillColor;
        this.$data.myChart.update();
      }
      this.$data.data = newVal;
    },
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
    width: 35vw;
    max-width: 1200px;
    min-width: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
    height: 50vh;
  }
  .labels-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 5px auto;
  }
  .lables {
    padding: 5px;
    margin: 5px;
    border: 1px solid black;
    border-radius: 25px;
  }
    img {
    /* Style for "Layer 32" */
			width: 15px;
			height: 15px;
			object-fit: cover;
  }
</style>