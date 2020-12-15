<template>
  <left-text :title="`${text.profile.mainTitle}`"/>
  <profile-groups />
  <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="monthlyData" id="monthly"/></div>
  <left-text :text="`${text.text2.text}`" :title= "`${text.text2.title}`"/>
  <div class="visualisations"><bar :data="top100Data" id="hashtags"/></div>
</template>

<script>
import Views from './../Views.vue'
import text from './../../assets/text.js'
import LeftText from './../LeftText.vue'
import ProfileGroups from './../ProfileGroups.vue'
import Bar from './../Charts/Bar.vue'
import monthlyData from './../Charts/data.js'
import top100Data from './../Charts/top100data.js'

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
      monthlyData,
      top100Data
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