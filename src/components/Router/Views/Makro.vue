<template>
  <div class="container-text">
    <p>Analize 4 različnih skupin Twitter uporabnikov, ki jih je mogoče primerjati med sabo. Analiza zajema čas od 1. 11. 2019 do 1.11. 2020.</p>
  </div>
  <profile-groups />
  <div class="container-text">
    <h2>Aktivnost</h2>
    <p>Število tvitov in ritvitov, ustvarjenih skozi čas glede na skupino.</p>
  </div>
  <div class="visualisations"><bar :data="tweetsByMonth" id="monthly"/></div>

  <!-- TOP HASHTAGS -->
  <div class="container-text">
    <h2>Top ključniki</h2>
    <p>Lestvice 30 najbolj pogosto uporabljenih ključnikov glede na skupino.</p>
  </div>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30Sample" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="hashtagsSample"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30500" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="hashtags500"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30Politiki" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="hashtagsPolitiki"/>
    </div>
        <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30Trolls" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="hashtagsTrolls"/>
    </div>
  </div>
  <div class="container-text">
    <h2>Top omembe</h2>
    <p>Lestvice 30 najbolj pogosto omenjenih uporabnikov glede na skupino.</p>
  </div>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30Sample" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="mentionsSample"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30500" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="mentions500"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30Politiki" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="mentionsPolitiki"/>
    </div>
        <div class="visualisations-group">
      <bar-custom :data="mentionsTop30Trolls" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="mentionsTrolls"/>
    </div>
  </div>
  <div class="container-text">
    <h2>Top RT</h2>
    <p>Lestvice 30 najbolj pogosto poobjavljenih uporabnikov glede na skupino.</p>
  </div>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30Sample" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="retweetsSample"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30500" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="retweets500"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30Politiki" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="retweetsPolitiki"/>
    </div>
        <div class="visualisations-group">
      <bar-custom :data="retweetsTop30Trolls" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="retweetsTrolls"/>
    </div>
  </div>
  <div class="container-text">
    <h2>Top domene</h2>
    <p>Lestvice 30 najbolj pogosto objavljenih domen glede na skupino.</p>
  </div>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30Sample" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="domainsSample"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30500" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="domains500"/>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30Politiki" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="domainsPolitiki"/>
    </div>
        <div class="visualisations-group">
      <bar-custom :data="domainsTop30Trolls" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="domainsTrolls"/>
    </div>
  </div>
</template>

<script>
import text from '../../../assets/text.js'
import BodyContentText from '../../BodyContentText.vue'
import ProfileGroups from '../../ProfileGroups.vue'
import Bar from '../../Charts/Bar.vue'
import BarCustom from '../../Charts/BarCustom.vue'
import tweetsByMonth from '../../Charts/tweetsByMonth.js'

import hashtagsTop30Sample from '../../../assets/charts/sample_hashtags.json';
import hashtagsTop30500 from '../../../assets/charts/500_hashtags.json';
import hashtagsTop30Politiki from '../../../assets/charts/politiki_hashtags.json';
import hashtagsTop30Trolls from '../../../assets/charts/trolls_hashtags.json';

import mentionsTop30Sample from '../../../assets/charts/sample_mentions.json';
import mentionsTop30500 from '../../../assets/charts/500_mentions.json';
import mentionsTop30Politiki from '../../../assets/charts/politiki_mentions.json';
import mentionsTop30Trolls from '../../../assets/charts/trolls_mentions.json';

import retweetsTop30Sample from '../../../assets/charts/sample_RT.json';
import retweetsTop30500 from '../../../assets/charts/500_RT.json';
import retweetsTop30Politiki from '../../../assets/charts/politiki_RT.json';
import retweetsTop30Trolls from '../../../assets/charts/trolls_RT.json';

import domainsTop30Sample from '../../../assets/charts/sample_domains.json';
import domainsTop30500 from '../../../assets/charts/500_domains.json';
import domainsTop30Politiki from '../../../assets/charts/politiki_domains.json';
import domainsTop30Trolls from '../../../assets/charts/trolls_domains.json';

export default {
  props: ["view"],
  components: {
    BodyContentText,
    ProfileGroups,
    Bar,
    BarCustom
  },
  data() {
    return {
      text: text.default,

      hashtagsTop30Sample,
      hashtagsTop30500,
      hashtagsTop30Politiki,
      hashtagsTop30Trolls,

      mentionsTop30Sample,
      mentionsTop30500,
      mentionsTop30Politiki,
      mentionsTop30Trolls,

      retweetsTop30Sample,
      retweetsTop30500,
      retweetsTop30Politiki,
      retweetsTop30Trolls,

      domainsTop30Sample,
      domainsTop30500,
      domainsTop30Politiki,
      domainsTop30Trolls,

      tweetsByMonth,
     }
  },
    methods: {
				updateChart(dataset, chart) {
					this.$router.push(route);
				}
			}
}
</script>

<style scoped>
@media only screen and (max-width: 768px) {
    .visualisations-group {
      width: 90vw;
      max-width: 1200px;
      min-width: 400px;
      height: 50vh;

    }
  }

  @media only screen and (min-width: 769px) {
    .visualisations-group {
      width: 45vw;
      max-width: 1200px;
      min-width: 500px;
      height: 50vh;
    }
  }
  .visualisations-container {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-wrap:  wrap 

  }
  .labels-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 5px auto;
  }
  .lables {
    padding: 5px;
    margin: 5px;
    border: 1px solid black;
    border-radius: 25px;
  }
  .visualisations {
    margin: 0 auto;
    width: 80vw;
    max-width: 1200px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
    height: 50vh;
  }
  .visualisations-group {
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column
  }
  .visualisations canvas {
    flex-shrink: 0;
    width: 90%;
    height: 90%
}
</style>