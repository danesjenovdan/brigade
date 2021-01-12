<template>
	<div class="container-text">
		<p>Analize 27 profilov, za katere obstaja visoka verjetnost, da so lažni in del organizirane mreže, saj uporabljajo ukradene, stock ali strojno generirane profilne slike, obenem pa se izdajajo za avtentične uporabnike in ustvarjajo velik delež vsebin in interakcij z jasno politično motivirano vsebino.</p>
	</div>
	<div class="mikro-container">
		<troll-profile-navigation @clicked="onClickChild"/>
	</div>
	<body-content-text>
		<template v-slot:title>
			Profil Twitter trolla
		</template>
	</body-content-text>
	<div class="visualisations-container">
		<troll-profile v-if="troll.accountInfo.name" :info="troll.accountInfo"/>
		<div class="visualisations"><bar :data="charts.retweets" id="temp"/></div>
	</div>
	<div v-if="troll.accountInfo.name" class="visualisations-container">
		<div class="visualisations"><bar :data="charts.retweets" id="retweets"/></div>
		<div class="visualisations"><bar :data="charts.replies" id="replies"/></div>
		<div class="visualisations"><bar :data="charts.mentions" id="mentions"/></div>
		<div class="visualisations"><bar :data="charts.hashtags" id="hashtags"/></div>
	</div>
  <body-content-text> bla bla bla </body-content-text>
	<fake-real-image :originalImage="originalImage" :stolenImage="stolenImage"/>
  <body-content-text> bla bla bla </body-content-text>
	<fake-real-image :originalImage="originalImage" :stolenImage="stolenImage"/>
</template>

<script>
import TrollProfileNavigation from './../../Trolls/ProfileNavigation.vue'
import BodyContentText from './../../BodyContentText.vue'
import TrollProfile from "./../../Trolls/Profile.vue"
import text from "./../../../assets/text.js"
import FakeRealImage from "./../../FakeRealImage.vue"
import Bar from './../../Charts/Bar.vue'
import createChartData from './../../Charts/createChartData'


export default {
  props: ["view"],
  components: {
    TrollProfileNavigation,
		BodyContentText,
		TrollProfile,
		FakeRealImage,
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
			this.$data.charts.retweets = createChartData(this.$data.troll, "retweets", 30, "retweets");
			this.$data.charts.replies = createChartData(this.$data.troll, "replies", 30, "Replies to user");
			this.$data.charts.mentions = createChartData(this.$data.troll, "mentions", 30, "Mentioned user");
			this.$data.charts.hashtags = createChartData(this.$data.troll, "hashtags", 30, "Used hashtags");

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