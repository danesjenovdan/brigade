<template>
  <left-text :title="`${profile.mainTitle}`"/>
  <profile-groups />
  <left-text :text="`${text2.text}`" :title= "`${text2.title}`"/>
  <div class="visualisations"><img alt="Vue logo" src="./../../assets/sample.png" /></div>
  <left-text :text="`${text2.text}`" :title= "`${text2.title}`"/>
  <div class="visualisations"><img alt="Vue logo" src="./../../assets/sample.png" /></div>
</template>

<script>
import Views from './../Views.vue'
import text from './../../assets/text.js'
import LeftText from './../LeftText.vue'
import ProfileGroups from './../ProfileGroups.vue'


export default {
  name: 'App',
  props: ["view"],
  components: {
    LeftText,
    ProfileGroups
  },
  data() {
    return text
  }
}
</script>