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
  <div class="visualisations"><bar :data="getTop30(hashtagTop100)" id="hashtags"/></div>
  <div class="visualisations"><bar :data="getTop30(mentionsTop100)" id="mentions"/></div>
  <div class="visualisations"><bar :data="getTop30(repliesTop100)" id="replies"/></div>
  <div class="visualisations"><bar :data="getTop30(retweetsTop100)" id="retweets"/></div>
</template>

<script>
import Views from './../Views.vue'
import * as text from './../../assets/text.js'
import BodyContentText from './../BodyContentText.vue'
import ProfileGroups from './../ProfileGroups.vue'
import Bar from './../Charts/Bar.vue'
import tweetsByMonth from './../Charts/tweetsByMonth.js'
import hashtagTop100 from './../Charts/hashtagTop100.js'
import mentionsTop100 from './../Charts/mentionsTop100.js'
import repliesTop100 from './../Charts/repliesTop100.js'
import retweetsTop100 from './../Charts/retweetsTop100.js'

export default {
  props: ["view"],
  components: {
    BodyContentText,
    ProfileGroups,
    Bar
  },
  data() {
    console.log(text);
    return { 
      text: text.default,
      tweetsByMonth,
      hashtagTop100,
      mentionsTop100,
      repliesTop100,
      retweetsTop100
     }
  },
  methods: {
    getTop30(top100) {
      const top30Labels = top100.data.labels.slice(0, 30);
      const top30LabelScores = top100.data.datasets[0].data.slice(0, 30);

      const top30 = { ...top100 }
      top30.data.labels = top30Labels;
      top30.data.datasets[0].data = top30LabelScores;

      return top30;
    },
  },
}
</script>

<style scoped>
  .visualisations {
    margin: 0 auto;
    width: 80vw;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    background-color: "black";
  }
  .visualisations canvas {
    flex-shrink: 0;
    width: 90%;
    height: 90%
}
</style>