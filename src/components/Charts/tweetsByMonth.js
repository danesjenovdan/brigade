export default {
    type: 'bar',
    data: {
      labels: [ '2019-10',
      '2019-11',
      '2019-12',
      '2020-01',
      '2020-02',
      '2020-03',
      '2020-04',
      '2020-05',
      '2020-06',
      '2020-07',
      '2020-08',
      '2020-09',
      '2020-10',
      '2020-11'],
      datasets: [
        { // another line graph
          label: 'Activity (number of tweets) by month of 500 NGO-supplied suspected trolls',
          data: [ 47632,
            54821,
            56416,
            68092,
            80415,
            127599,
            149260,
            272417,
            261061,
            275270,
            232852,
            221185,
            284904,
            141361]
          ,
          backgroundColor: 'rgb(92, 134, 74)', // Green
          borderColor: '#5c864a',
          borderWidth: 3
        },
        { // another line graph
          label: 'Activity (number of tweets) by leftist',
          data: [ 47632,
            34821,
            46416,
            78092,
            40415,
            17599,
            129260,
            572417,
            761061,
            375270,
            732852,
            821185,
            684904,
            241361]
          ,
          backgroundColor: 'rgb(90, 164, 214)', // Green
          borderColor: '#5aa4d6',
          borderWidth: 3
        },
        { // another line graph
          label: 'Activity (number of tweets) by right wingers',
          data: [ 67632,
            44821,
            76416,
            38092,
            50415,
            37599,
            129260,
            472417,
            961061,
            775270,
            232852,
            321185,
            484904,
            541361]
          ,
          backgroundColor: 'rgb(234, 110, 51)', // Green
          borderColor: '#ea6e33',
          borderWidth: 3
        },
        { // another line graph
          label: 'Activity (number of tweets) by control goup',
          data: [ 67632,
            44821,
            76416,
            38092,
            50415,
            47599,
            29260,
            272417,
            561061,
            275270,
            332852,
            321185,
            284904,
            41361]
          ,
          backgroundColor: 'rgb(249, 233, 111)', // Green
          borderColor: '#f9e96f',
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
          }
        }]
      }
    }
  }
  