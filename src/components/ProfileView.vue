<template>
		<div class="flex-grid">
			<user-round class="flex-grid-item" v-for="troll in text.trolls" :imageUrl="troll.imageUrl" :name="troll.name" :id="troll.id"></user-round>
		</div>
</template>

<script>
import UserRound from './UserRound.vue'
import text from '../assets/text.js'

export default {
  components: {
    UserRound
  },
	data() {
		return {
			text
		}
	}

}
</script>

<style scoped>
@media only screen and (max-width: 768px) {
	.flex-grid {
		max-width: 80vw;
		display: flex;
		overflow-x: auto;
  }
}
@media only screen and (min-width: 769px) {
	.flex-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
  }
  .flex-grid-item {
    flex-grow: 0;
    flex-shrink: 0;
    align-items: center;
  }
}
</style>