export default {
    type: 'horizontalBar',
    data: {
      labels:  [ 'Jo_AnnaOfArt',
      'vinkovasle1',
      'ErikaPlaninsec',
      'BojanPozar',
      'zasledovalec70',
      'hrastelj',
      'MatevzNovak',
      'martinvalic',
      'JakaDolinar2',
      'mrevlje',
      'BizjakSelma',
      'MarkoSket',
      'JozeBizjak',
      'MetkaSmole',
      'cesenj',
      'Stanisl15592752',
      'lojzi1',
      'tfajon',
      'nivelska',
      'tomltoml',
      'BojankaStern',
      'SamoGlavan',
      'cikibucka',
      'MarkoFratnik',
      'JJansaSDS',
      'strankaSD',
      'DesnicarkaM',
      'Leon48303573',
      'SlovenijaVsrcu',
      'Medeja_7',
      'GPreac']
    ,
      datasets: [
        { // another line graph
          label: 'Activity (most replies to user) by month of 500 NGO-supplied suspected trolls',
          data: [ 18368,
            7888,
            7877,
            7214,
            7203,
            6248,
            6171,
            5662,
            5544,
            4838,
            4653,
            4637,
            4615,
            4569,
            4569,
            4531,
            4115,
            4067,
            3944,
            3942,
            3927,
            3892,
            3872,
            3835,
            3824,
            3810,
            3800,
            3725,
            3711,
            3704,
            3646]          
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
  