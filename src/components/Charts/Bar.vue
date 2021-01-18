<template>
  <canvas :id="id"></canvas>
</template>

<script>
import Chart from 'chart.js';

export default {
  name: "Bar",
    props: {
      id: { type: String, required: true },
      data: { type: Object, required: true },
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
      }
  },
  mounted() {
    if (this.data) { 
      console.log('this.id: ', this.id);
      this.createChart(this.id, this.data);
      }
  },
   watch: {
    data(newVal) {
      if (!this.$data.data)  {
        this.createChart(this.id, newVal);
      } else {
        console.log("update", this.id)
        this.$data.myChart.data.labels = newVal.data.labels;
        this.$data.myChart.data.datasets = newVal.data.datasets
        this.$data.myChart.update();
      }
      this.$data.data = newVal;
    },
  },
};
</script>