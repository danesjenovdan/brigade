<template>
  <profile-groups />
  <body-content-text>
    <template v-slot:title>
      Aktivnost
    </template>
    Število tvitov in ritvitov, ustvarjenih skozi čas glede na skupino.
  </body-content-text>
  <div class="visualisations-container">
    <bar-with-custom-labels :data="tweetsByMonth" id="monthly"/>
  </div>
  <!-- TOP HASHTAGS -->
  <body-content-text>
    <template v-slot:title>
      Top ključniki
    </template>
    Lestvice 20 najbolj pogosto uporabljenih ključnikov glede na skupino.
  </body-content-text>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30Trolls" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="hashtagsTrolls" :displayLabel="false"> <img alt="" src="/red.png"/> Lažni profili</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30500" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="hashtags500" :displayLabel="false"> <img alt="" src="/green.png"/> Brigada</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30Politiki" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="hashtagsPolitiki" :displayLabel="false"><img alt="" src="/blue.png"/> Politiki</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="hashtagsTop30Sample" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="hashtagsSample" :displayLabel="false"> <img alt="" src="/yellow.png"/> Kontrolni vzorec </bar-custom>
    </div>
  </div>
  <body-content-text>
    <template v-slot:title>
      Top omembe
    </template>
    Lestvice 20 najbolj pogosto omenjenih uporabnikov glede na skupino.
  </body-content-text>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30Trolls" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="mentionsTrolls" :displayLabel="false"> <img alt="" src="/red.png"/> Lažni profili</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30500" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="mentions500" :displayLabel="false"><img alt="" src="/green.png"/> Brigada</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30Politiki" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="mentionsPolitiki" :displayLabel="false"><img alt="" src="/blue.png"/> Politiki</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="mentionsTop30Sample" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="mentionsSample" :displayLabel="false"> <img alt="" src="/yellow.png"/> Kontrolni vzorec </bar-custom>
    </div>
  </div>
  <body-content-text>
    <template v-slot:title>
      Top RT
    </template>
      Lestvice 20 najbolj pogosto poobjavljenih uporabnikov glede na skupino.
  </body-content-text>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30Trolls" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="retweetsTrolls" :displayLabel="false"> <img alt="" src="/red.png"/> Lažni profili</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30500" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="retweets500" :displayLabel="false"> <img alt="" src="/green.png"/> Brigada</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30Politiki" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="retweetsPolitiki" :displayLabel="false"><img alt="" src="/blue.png"/> Politiki</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="retweetsTop30Sample" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="retweetsSample" :displayLabel="false"> <img alt="" src="/yellow.png"/> Kontrolni vzorec</bar-custom>
    </div>
  </div>
  <body-content-text>
    <template v-slot:title>
      Top domene
    </template>
      Lestvice 20 najbolj pogosto objavljenih domen glede na skupino.
  </body-content-text>
  <div class="visualisations-container">
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30Trolls" borderColor='rgb(234, 110, 51)'
        fillColor='#ea6e33' id="domainsTrolls" :displayLabel="false"> <img alt="" src="/red.png"/> Lažni profili</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30500" borderColor='rgb(92, 134, 74)'
        fillColor='#5c864a' id="domains500" :displayLabel="false"> <img alt="" src="/green.png"/> Brigada</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30Politiki" borderColor='rgb(90, 164, 214)'
        fillColor='#5aa4d6' id="domainsPolitiki" :displayLabel="false"><img alt="" src="/blue.png"/> Politiki</bar-custom>
    </div>
    <div class="visualisations-group">
      <bar-custom :data="domainsTop30Sample" borderColor='rgb(249, 233, 111)'
        fillColor='#f9e96f' id="domainsSample" :displayLabel="false"> <img alt="" src="/yellow.png"/> Kontrolni vzorec</bar-custom>
    </div>
  </div>
</template>

<script>
import text from '../../../assets/text.js'
import BodyContentText from '../../BodyContentText.vue'
import ProfileGroups from '../../ProfileGroups.vue'
import Bar from '../../Charts/Bar.vue'
import BarCustom from '../../Charts/BarCustom.vue'
import BarWithCustomLabels from '../../Charts/BarWithCustomLabels.vue'
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
    BarCustom,
    BarWithCustomLabels
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
      height: 60vh;

    }
  }

  @media only screen and (min-width: 769px) {
    .visualisations-group {
      width: 35vw;
      max-width: 1200px;
      min-width: 500px;
      height: 60vh;
    }
  }
  .visualisations-container {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-wrap:  wrap ;
    width: 80vw;
    margin-bottom: 50px;
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
    min-width: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
  }
  .visualisations-group {
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
  }
  .visualisations canvas {
    flex-shrink: 0;
    width: 90%;
    height: 90%
}
img {
  height: 15px;
  width: 15ox;
  margin-right: 5px;
}
</style>