export default {
    type: 'bar',
    data: {
      labels: ['Januar 2020',
      'Februar 2020',
      'Marec 2020',
      'April 2020',
      'Maj 2020',
      'Junij 2020',
      'Julij 2020',
      'Avgust 2020',
      'September 2020',
      'Oktober 2020',
      'Nobember 2020',
      'December 2020'],
      datasets: [
        { // another line graph
          label: 'Activity (number of tweets) by fake profiles',
          // data: [2791, 3808, 5939, 3812, 3835, 4750, 5183, 3251, 3040, 4237, 3470, 3650],
          data: [107.34615384615384, 146.46153846153845, 228.42307692307693, 146.6153846153846, 147.5, 182.69230769230768, 199.34615384615384, 125.03846153846153, 116.92307692307692, 162.96153846153845, 133.46153846153845, 140.3846153846154],
          backgroundColor: 'rgb(234, 110, 51)',
          borderColor: '#ea6e33',
          borderWidth: 3,
          id: 'fake'
        },
        { // another line graph
          label: 'Activity (number of tweets) by month of 500 NGO-supplied suspected trolls',
          // data: [72052, 86396, 133356, 118984, 118773, 101301, 103850, 92687, 99589, 145666, 169295, 204505],
          data: [144.104, 172.792, 266.712, 237.968, 237.546, 202.602, 207.7, 185.374, 199.178, 291.332, 338.59, 409.01],
          backgroundColor: 'rgb(92, 134, 74)',
          borderColor: '#5c864a',
          borderWidth: 3,
          id: 'brigade'
        },
        { // another line graph
          label: 'Activity (number of tweets) by politicians',
                  // data: [3113, 4337, 7962, 7759, 7678, 5872, 6321, 4623, 6328, 9470, 10851, 12245],
          data: [35.7816091954023, 49.85057471264368, 91.51724137931035, 89.183908045977, 88.25287356321839, 67.49425287356321, 72.65517241379311, 53.13793103448276, 72.73563218390805, 108.85057471264368, 124.72413793103448, 140.7471264367816],
          backgroundColor: 'rgb(90, 164, 214)',
          borderColor: '#5aa4d6',
          borderWidth: 3,
          id: 'politiki'
        },
        { // another line graph
          label: 'Activity (number of tweets) by control goup',
          // data: [17739, 17070, 26898, 22723, 20346, 20798, 22247, 23910, 29475, 30219, 29923, 29598],
          data: [147.825, 142.25, 224.15, 189.35833333333332, 169.55, 173.31666666666666, 185.39166666666668, 199.25, 245.625, 251.825, 249.35833333333332, 246.65],
          backgroundColor: 'rgb(249, 233, 111)', // Green
          borderColor: '#f9e96f',
          borderWidth: 3,
          id: 'control'
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
          }
        }]
      }
    }
  }
  