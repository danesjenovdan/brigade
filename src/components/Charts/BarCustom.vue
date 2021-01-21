<template>
  <canvas :id="id"></canvas>
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
			borderColor: { type: String }
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
				if (firstPoint !== undefined)
				window.open("https://twitter.com/hashtag/"+label, '_blank');
		};
      }
  },
  mounted() {
    if (this.data) { 
			const simpleData = createSimpleData(this.data.values, 30, this.data.labels)
			const configured = configure(this.data.data.labels,
			this.data.data.datasets[0].label,
			this.data.data.datasets[0].data,
			this.borderColor,
			this.fillColor,
			this.id
			)
      this.createChart(this.id, configured);
      }
  },
};
</script>

<style scoped>
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