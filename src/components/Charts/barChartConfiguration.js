export const configue = (labels, label, data, backgroundColor, borderColor, id, displayLegend) => { return {
    type: 'horizontalBar',
    data: {
      labels,    
      datasets: [
        { // another line graph
          label: label,
          data: data,
          backgroundColor: backgroundColor, // Green
          borderColor: borderColor,
          borderWidth: 3
        }
      ]
    },
    options: {
      maintainAspectRatio: false,
      legend: {
        display: displayLegend,
        usePointStyle: true
        },
      responsive: true,
      lineTension: 1,
      scales: {
        yAxes: [{
          afterFit: function(scaleInstance) {
            scaleInstance.width = 210; // sets the width to 100px
          },
          ticks: {
            beginAtZero: true,
            padding: 25,
            autoSkip: false,
            fontSize: 16,
            callback: function (tick) {
              if (tick.includes("www.")) return tick.replace("www.", "");
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
  }
}
  
  export default configue;