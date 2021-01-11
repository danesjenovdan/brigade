export const planetChartData = {
    type: 'horizontalBar',
    data: {
      labels: [ 'COVID19',
      'Požareport',
      'koronavirus',
      'Slovenia',
      'OstaniZdrav',
      'govoricatelesa',
      'EU',
      'Covid_19',
      'coronavirus',
      'sampovem',
      'levuhad',
      'Slovenija',
      'Covid19',
      'MSM',
      'žilneopornice',
      'Antifa',
      'DeltaLifeCoaching',
      'tako',
      'tvit',
      'dober',
      'porušitiRTVHanzi',
      'video',
      'covid19',
      'bucibuc',
      'ronikordis',
      'TDF2020',
      'dan',
      'vsak',
      'komunikacija',
      'NPU',
      'BlackLivesMatter',
      ],    
      datasets: [
        { // another line graph
          label: 'Top hashtags of 500 NGO-supplied suspected trolls',
          data: [ 5031,
            3342,
            2345,
            1523,
            1389,
            1324,
            1234,
            1170,
            1024,
            993,
            984,
            979,
            934,
            764,
            733,
            710,
            699,
            659,
            645,
            641,
            629,
            619,
            617,
            605,
            594,
            559,
            530,
            527,
            519,
            501,
            497,
            ]
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
  
  export default planetChartData;