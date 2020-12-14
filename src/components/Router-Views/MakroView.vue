<template>
  <left-text :title="`${profile.mainTitle}`"/>
  <profile-groups />
  <left-text :text="`${text2.text}`" :title= "`${text2.title}`"/>
  <div class="visualisations"><bar/></div>
  <left-text :text="`${text2.text}`" :title= "`${text2.title}`"/>
</template>

<script>
import Views from './../Views.vue'
import text from './../../assets/text.js'
import LeftText from './../LeftText.vue'
import ProfileGroups from './../ProfileGroups.vue'
import Bar from './../Charts/Bar.vue'


export default {
  name: 'App',
  props: ["view"],
  components: {
    LeftText,
    ProfileGroups,
    Bar
  },
  data() {
    return text
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