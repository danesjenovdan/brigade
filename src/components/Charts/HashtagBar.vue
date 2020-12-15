<template>
    <canvas id="hashtagBar"></canvas>
  </template>

<script>
import Chart from 'chart.js';
import data from './top100data.js';

export default {
  name: "Bar",
  data() {
    return {
      data: data,
    }
  },
    methods: {
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
      });
    }
  },
  mounted() {
    this.createChart('hashtagBar', this.data);
  }
};
</script>