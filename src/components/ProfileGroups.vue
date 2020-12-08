<template>
	<div class="flex-grid">
		<profile class="flex-grid-item" :title="`${profile.control.title}`" :subtitle="`${profile.subtitle}`" :text="`${text}`" imageUrl="src/assets/yellow.png"></profile>
		<profile class="flex-grid-item" :title="`${profile.fake.title}`" :subtitle="`${profile.subtitle}`" :text="`${text}`" imageUrl="src/assets/green.png"></profile>
		<profile class="flex-grid-item" :title="`${profile.right.title}`" :subtitle="`${profile.subtitle}`" :text="`${text}`" imageUrl="src/assets/red.png"></profile>
		<profile class="flex-grid-item" :title="`${profile.left.title}`" :subtitle="`${profile.subtitle}`" :text="`${text}`" imageUrl="src/assets/blue.png"></profile>
	</div >
</template>

<script>
import Profile from './Profile.vue'
import text from './../assets/text.js'

export default {
  components: {
    Profile
  },
  data() {
    return text
  } 
}
</script>

<style scoped>
	.flex-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
  }

  .flex-grid-item {
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: 13%;
    margin-left: 50px;
		margin-right: 50px;
    align-items: center;
  }
</style>