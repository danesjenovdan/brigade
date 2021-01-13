<template>
		<div class="flex-grid">
				<profile-picture @clicked="onClickChild" class="flex-grid-item"
				v-for="troll in trolls"
				:imageUrl="troll.accountInfo.imageUrl"
				:name="troll.accountInfo.name"
				:clicked = "troll.accountInfo.name === clickedName"
				:info = "troll.accountInfo"
				/>
		</div>
</template>

<script>
import ProfilePicture from './ProfilePicture.vue'
import troll1 from '../../assets/trolls/desnicarkaminfo.json'
import troll2 from '../../assets/trolls/karolinasemjazinfo.json'

export default {
  components: {
    ProfilePicture
  },
	data() {
		return {
			trolls: [
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
				troll1,
				troll2,
			],
			clickedName: ""
		}
	},
	methods: {
    onClickChild (value) {
      this.clickedName = value.name; // someValue
			this.$emit('clicked', this.$data.trolls.find(element => element.accountInfo.name === value.name));
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
		width: 80vw;
  }
  .flex-grid-item {
    flex-grow: 0;
    flex-shrink: 0;
    align-items: center;
  }
}
</style>