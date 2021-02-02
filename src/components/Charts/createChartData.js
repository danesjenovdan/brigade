export default (troll = {}, type = "", size = 0, label="", backgroundColor, borderColor) => {
  console.log(troll, type);
	troll = Object.entries(troll[type]);
	troll.sort(function (a, b) {
		return b[1] - a[1];
	}).splice(size);
	const labels = [];
	const data = []
	troll.forEach(element => {
		labels.push(element[0])
		data.push(element[1])
	});
	
	return {
    type: 'horizontalBar',
    data: {
      labels,    
      datasets: [
        { // another line graph
          label,
          data,
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
            fontSize: 10
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