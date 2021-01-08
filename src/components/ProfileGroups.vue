<template>
	<div class="flex-grid">
		<profile class="flex-grid-item" :title="`${groups.control.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/yellow.png"/>
		<profile class="flex-grid-item" :title="`${groups.fake.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/green.png"/>
		<profile class="flex-grid-item" :title="`${groups.right.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/red.png"/>
		<profile class="flex-grid-item" :title="`${groups.left.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/blue.png"/>
	</div >
</template>

<script>
import Profile from './Trolls/Profile.vue' // generilized component that can be used for troll type card
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
    margin-left: 25px;
		margin-right: 25px;
    align-items: center;
  }
</style>