export default {
    type: 'horizontalBar',
    data: {
      labels: [ 'JJansaSDS',
      'Jo_AnnaOfArt',
      'vladaRS',
      'BojanPozar',
      'RTV_Slovenija',
      'Nova24TV',
      'strankaSD',
      'vinkovasle1',
      'sarecmarjan',
      'tfajon',
      'aleshojs',
      'policija_si',
      'rtvslo',
      'strankalevica',
      'ZigaTurk',
      'mrevlje',
      'JakaDolinar2',
      'strankaSDS',
      'Demokracija1',
      'Libertarec',
      'VaneGosnik',
      'hrastelj',
      'DKopse',
      'ErikaPlaninsec',
      'StrankaLMS',
      'JozeBiscak',
      'MarkoSket',
      'Medeja_7',
      'zasledovalec70',
      'tomltoml',
      'Pertinacal',
      ],
      datasets: [
        { // another line graph
          label: 'Number of mentions of 500 NGO-supplied suspected trolls',
          data: [ 101600,
            67030,
            63835,
            45144,
            40807,
            39464,
            38827,
            34397,
            31430,
            31208,
            23757,
            21825,
            20853,
            20841,
            20543,
            19232,
            18728,
            17218,
            17000,
            15749,
            15441,
            15007,
            14909,
            14708,
            14578,
            14074,
            13854,
            13727,
            13706,
            13662,
            13412
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
  