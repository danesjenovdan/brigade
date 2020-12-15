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
    methods: {
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      ctx.fillStyle = 'white';
      ctx.style.backgroundColor = 'white';
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
      });
    }
  },
  mounted() {
    this.createChart(this.id, this.data);
  }
};
</script>