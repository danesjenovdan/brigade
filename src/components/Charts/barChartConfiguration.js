export const configue = (labels, label, data, backgroundColor, borderColor, id) => { return {
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
  }
}
  
  export default configue;