export default (troll = {}, type = "", size = 0, label="", backgroundColor, borderColor) => {
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
          backgroundColor: 'rgba(71, 183,132,.5)', // Green
          borderColor: '#47b784',
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      lineTension: 1,
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true,
            padding: 25,
          }
        }]
      }
    }
  }
}