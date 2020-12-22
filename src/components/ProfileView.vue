<template>
		<div class="flex-grid">
				<user-round @clicked="onClickChild" class="flex-grid-item"
				v-for="troll in text.trolls"
				:imageUrl="troll.imageUrl"
				:name="troll.name"
				:id="troll.id"
				:clicked = "troll.id === clickedId"
				>
				</user-round>
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
			text,
			clickedId: ""
		}
	},
	methods: {
    onClickChild (value) {
      this.clickedId = value; // someValue
			this.$emit('clicked', this.clickedId)
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