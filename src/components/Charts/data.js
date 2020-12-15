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
  