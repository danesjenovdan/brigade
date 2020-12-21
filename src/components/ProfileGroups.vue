<template>
	<div class="flex-grid">
		<groups class="flex-grid-item" :title="`${groups.control.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/yellow.png"></groups>
		<groups class="flex-grid-item" :title="`${groups.fake.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/green.png"></groups>
		<groups class="flex-grid-item" :title="`${groups.right.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/red.png"></groups>
		<groups class="flex-grid-item" :title="`${groups.left.title}`" :subtitle="`${groups.subtitle}`" :text="`${text}`" imageUrl="/blue.png"></groups>
	</div >
</template>

<script>
import Groups from './Groups.vue'
import text from './../assets/text.js'

export default {
  components: {
    Groups
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