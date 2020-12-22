<template>
	<div class="mikro-container">
		<profile-view></profile-view>
	</div>
	<left-text title="Profil Twitter trolla"/>
	<groups :info="info"/>
  <left-text :text="`${text.text2.text}`"/>
	<stolen-picture :originalImage="originalImage" :stolenImage="stolenImage"></stolen-picture>
</template>

<script>
import ProfileView from '../ProfileView.vue'
import LeftText from './../LeftText.vue'
import Groups from "../Groups.vue"
import text from "./../../assets/text.js"
import StolenPicture from "../StolenPicture.vue"

export default {
  props: ["view"],
  components: {
    ProfileView,
		LeftText,
		Groups,
		StolenPicture
  },
	data() {
		return {
			info: {
				nFollowers: "5",
				nFollowing:"10",
				nTweets: "5",
				registrationDate: "2020.20.19",
				location: "Ljubljana",
				imageUrl: "https://innovationorigins.com/app/uploads/2019/12/monkee-1024x683-1004x670.jpg",
				name: "Opica 1"
			},
			text,
			originalImage: {
				imageUrl: "https://media.npr.org/assets/img/2015/09/23/ap_836720500193-13f1674f764e5180cf9f3349cfef258d181f2b32-s800-c85.jpg",
				sourceUrl: "https://www.rickroll.com",
				text: "Monkeeeee"

			},
			stolenImage: {
				imageUrl: "https://specials-images.forbesimg.com/imageserve/1160859961/960x0.jpg?fit=scale",
				sourceUrl: "https://www.rickroll.com",
				text: "@Monkeeeeee"
			}
		}
	} 
}
</script>

<style scoped>
  .mikro-container {
		border-top: 1px solid #b0b0b0;
		border-bottom: 1px solid #b0b0b0;
    margin: auto 5%;
  }
</style>