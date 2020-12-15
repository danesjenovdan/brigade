<template>
  <left-text :title="`${text.profile.mainTitle}`"/>
  <profile-groups />
  <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="tweetsByMonth" id="monthly"/></div>
  <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="hashtagTop100" id="hashtags"/></div>
  <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="mentionsTop100" id="mentions"/></div>
    <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="repliesTop100" id="replies"/></div>
    <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="retweetsTop100" id="retweets"/></div>
</template>

<script>
import Views from './../Views.vue'
import text from './../../assets/text.js'
import LeftText from './../LeftText.vue'
import ProfileGroups from './../ProfileGroups.vue'
import Bar from './../Charts/Bar.vue'
import tweetsByMonth from './../Charts/tweetsByMonth.js'
import hashtagTop100 from './../Charts/hashtagTop100.js'
import mentionsTop100 from './../Charts/mentionsTop100.js'
import repliesTop100 from './../Charts/repliesTop100.js'
import retweetsTop100 from './../Charts/retweetsTop100.js'


export default {
  name: 'App',
  props: ["view"],
  components: {
    LeftText,
    ProfileGroups,
    Bar
  },
  data() {
    return { 
      text,
      tweetsByMonth,
      hashtagTop100,
      mentionsTop100,
      repliesTop100,
      retweetsTop100
     }
  }
}
</script>

<style scoped>
  .visualisations {
    margin: 0 auto;
    width: 80%;
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