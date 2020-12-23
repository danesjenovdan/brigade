<template>
	<div class="mikro-container">
		<profile-view @clicked="onClickChild"></profile-view>
	</div>
	<left-text title="Profil Twitter trolla"/>
	<div class="visualisations-container">
		<groups v-if="troll.accountInfo.name" :info="troll.accountInfo"/>
		<div class="visualisations"><bar :data="charts.retweets" id="temp"/></div>
	</div>
	<div class="visualisations-container">
		<div class="visualisations"><bar :data="charts.retweets" id="retweets"/></div>
		<div class="visualisations"><bar :data="charts.replies" id="replies"/></div>
		<div class="visualisations"><bar :data="charts.mentions" id="mentions"/></div>
		<div class="visualisations"><bar :data="charts.hashtags" id="hashtags"/></div>
	</div>
  <left-text :text="`${text.text2.text}`"/>
	<stolen-picture :originalImage="originalImage" :stolenImage="stolenImage"></stolen-picture>
</template>

<script>
import ProfileView from '../ProfileView.vue'
import LeftText from './../LeftText.vue'
import Groups from "../Groups.vue"
import text from "./../../assets/text.js"
import StolenPicture from "../StolenPicture.vue"
import Bar from './../Charts/Bar.vue'
import createChartData from './../Charts/createChartData'


export default {
  props: ["view"],
  components: {
    ProfileView,
		LeftText,
		Groups,
		StolenPicture,
		Bar
  },
	data() {
		return {
			troll: {
				accountInfo: {
				}
			},
			charts: {
				replies: {},
				retweets: {},
				replies: {},
				hashtags: {}
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
	},
		methods: {
    onClickChild (value) {
			this.$data.troll = value;
			this.$data.charts.retweets = createChartData(this.$data.troll, "retweets", 20, "retweets");
			this.$data.charts.replies = createChartData(this.$data.troll, "replies", 20, "Replies to user");
			this.$data.charts.mentions = createChartData(this.$data.troll, "mentions", 20, "Mentioned user");
			this.$data.charts.hashtags = createChartData(this.$data.troll, "hashtags", 20, "Used hashtags");

    },
		createChartData
  }
}
</script>

<style scoped>
  .mikro-container {
		border-top: 1px solid #b0b0b0;
		border-bottom: 1px solid #b0b0b0;
    margin: auto 5%;
  }
	.visualisations-container {
		display: flex;
		flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;
		width: 80vw;
  }
	.visualisations {
    margin: 0 auto;
    width: 40vw;
		min-width: 400px;
    display: flex;
    justify-content: flex-start;
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