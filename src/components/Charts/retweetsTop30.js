export default {
    type: 'horizontalBar',
    data: {
      labels:  [ '@JJansaSDS',
      '@Jo_AnnaOfArt',
      '@BojanPozar',
      '@Nova24TV',
      '@vinkovasle1',
      '@Demokracija1',
      '@vladaRS',
      '@Libertarec',
      '@mrevlje',
      '@ZigaTurk',
      '@JakaDolinar2',
      '@VaneGosnik',
      '@JozeBiscak',
      '@DKopse',
      '@MitjaIrsic',
      '@tomltoml',
      '@LahovnikMatej',
      '@peterjancic',
      '@MarkoSket',
      '@aleshojs',
      '@strankaSDS',
      '@bmz9453',
      '@tradicijaslo',
      '@GPreac',
      '@BizjakSelma',
      '@mojcav1',
      '@rose_bayern',
      '@akashaanasha',
      '@petra_jansa',
      '@BesniUpokojenec',
      '@NeMaramButlov'],
      datasets: [
        { // another line graph
          label: 'Activity (number of retweets to user) by month of 500 NGO-supplied suspected trolls',
          data: [ 29462,
            21016,
            20946,
            13612,
            13211,
            11788,
            10732,
            9523,
            9135,
            9049,
            8720,
            8235,
            8088,
            7513,
            6355,
            6329,
            5815,
            5573,
            5521,
            5406,
            4956,
            4943,
            4935,
            4846,
            4759,
            4710,
            4706,
            4661,
            4589,
            4354,
            4246],
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
  