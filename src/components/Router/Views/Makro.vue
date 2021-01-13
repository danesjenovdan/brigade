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
  <div class="visualisations"><bar :data="hashtagTop30" id="hashtags"/></div>
  <div class="visualisations"><bar :data="mentionsTop30" id="mentions"/></div>
  <div class="visualisations"><bar :data="repliesTop30" id="replies"/></div>
  <div class="visualisations"><bar :data="retweetsTop30" id="retweets"/></div>
</template>

<script>
import text from './../../../assets/text.js'
import BodyContentText from './../../BodyContentText.vue'
import ProfileGroups from './../../ProfileGroups.vue'
import Bar from './../../Charts/Bar.vue'
import tweetsByMonth from './../../Charts/tweetsByMonth.js'
import hashtagTop30 from './../../Charts/hashtagTop30.js'
import mentionsTop30 from './../../Charts/mentionsTop30.js'
import repliesTop30 from './../../Charts/repliesTop30.js'
import retweetsTop30 from './../../Charts/retweetsTop30.js'

export default {
  props: ["view"],
  components: {
    BodyContentText,
    ProfileGroups,
    Bar
  },
  data() {
    return { 
      text: text.default,
      tweetsByMonth,
      hashtagTop30,
      mentionsTop30,
      repliesTop30,
      retweetsTop30
     }
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