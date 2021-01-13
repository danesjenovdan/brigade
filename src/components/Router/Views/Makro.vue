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
  <div class="container-text">
    <h2>Top lestvice</h2>
    <p>Lestvice 30 najbolj pogosto uporabljenih ključnikov, omemb, ritvitov in domen glede na skupino.</p>
  </div>
  <div class="visualisations">
    <bar-custom-labels :data="hashtag" id="hashtags"/>
  </div>
  <div class="visualisations"><bar :data="mentionsTop30" id="mentions"/></div>
  <div class="visualisations"><bar :data="repliesTop30" id="replies"/></div>
  <div class="visualisations"><bar :data="retweetsTop30" id="retweets"/></div>
</template>

<script>
import text from './../../../assets/text.js'
import BodyContentText from './../../BodyContentText.vue'
import ProfileGroups from './../../ProfileGroups.vue'
import Bar from './../../Charts/Bar.vue'
import BarCustomLabels from './../../Charts/BarCustomLabels.vue'
import tweetsByMonth from './../../Charts/tweetsByMonth.js'
import hashtagTop30 from './../../Charts/hashtag-500-30.json'
import hashtagTop30Politiki from './../../Charts/vsi-politiki-hashtags-30.json'
import mentionsTop30 from './../../Charts/mentionsTop30.js'
import repliesTop30 from './../../Charts/repliesTop30.js'
import retweetsTop30 from './../../Charts/retweetsTop30.js'

export default {
  props: ["view"],
  components: {
    BodyContentText,
    ProfileGroups,
    Bar,
    BarCustomLabels
  },
  data() {
    return { 
      text: text.default,
      hashtag: {
        data1: hashtagTop30Politiki,
        data2: hashtagTop30,
      },
      tweetsByMonth,
      mentionsTop30,
      repliesTop30,
      retweetsTop30,
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