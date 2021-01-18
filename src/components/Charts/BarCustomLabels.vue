<template>
    <div class="labels-container">
      <div @click="updateChart(data.data1, 'rgb(90, 164, 214)','#5aa4d6')" class="lables">
      <img alt="" src="/blue.png">
        politiki
      </div>
      <div  @click="updateChart(data.data2, 'rgb(92, 134, 74)', '#5c864a')" class="lables">
      <img alt="" src="/green.png">
        500 NGO-suspected trolls
      </div>
    </div>
  <canvas :id="id"></canvas>
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
      },
			updateChart(data, backgroundColor, borderColor) {
				this.$data.myChart.data.labels = data.data.labels;
				data.data.datasets[0].backgroundColor = backgroundColor;
				data.data.datasets[0].borderColor = borderColor;
        this.$data.myChart.data.datasets = data.data.datasets
        this.$data.myChart.update();
			}
  },
  mounted() {
    if (this.data) { 
			//const simpleData = createSimpleData(this.data.data1.values, 30, this.data.data1.labels)
			const configured = configure(this.data.data2.data.labels,
			this.data.data2.data.datasets[0].label,
			this.data.data2.data.datasets[0].data,
			'rgb(92, 134, 74)',
			'#5c864a', 
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