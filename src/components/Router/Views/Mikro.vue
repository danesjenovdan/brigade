<template>
	<div class="container-text">
		<p>Analize 27 profilov, za katere obstaja visoka verjetnost, da so lažni in del organizirane mreže, saj uporabljajo ukradene, stock ali strojno generirane profilne slike, obenem pa se izdajajo za avtentične uporabnike in ustvarjajo velik delež vsebin in interakcij z jasno politično motivirano vsebino.</p>
	</div>
	<div class="mikro-container">
		<troll-profile-navigation @clicked="onClickChild"/>
	</div>
	<body-content-text>
		<template v-slot:title>
		</template>
	</body-content-text>
	<div class="visualisations-container">
		<troll-profile v-if="troll.accountInfo.name" :info="troll.accountInfo"/>
		<div class="visualisations"><bar :data="charts.retweets" id="temp"/></div>
	</div>
	<div v-if="troll.accountInfo.name" class="visualisations-container">
		<div class="visualisations-group"><bar-custom :data="charts.retweets" borderColor='rgb(249, 233, 111)'
					fillColor='#f9e96f' id="retweets"/></div>
			<div class="visualisations-group"><bar-custom :data="charts.mentions" borderColor='rgb(90, 164, 214)'
				fillColor='#5aa4d6' id="mentions"/></div>
			<div class="visualisations-group"><bar-custom :data="charts.replies" borderColor='rgb(234, 110, 51)'
					fillColor='#ea6e33' id="replies"/></div>
			<div class="visualisations-group"><bar-custom :data="charts.hashtags" borderColor='rgb(92, 134, 74)'
				fillColor='#5c864a' id="hashtags"/></div>
	</div>
	<fake-real-image class="image-container" v-for="image in images">
		<img class="image" alt="" :src="'/27Trolov' + image.src" />
			<template v-slot:original>
					<i><a target="_blank" class="url" :href="image.leftLink">{{image.leftCaption}}</a></i>
		</template>
		<template v-slot:fake>
				<i><a target="_blank" class="url" :href="image.rightLink">{{image.rightCaption}}</a></i>
		</template>
	</fake-real-image>

</template>

<script>
import TrollProfileNavigation from './../../Trolls/ProfileNavigation.vue'
import BodyContentText from './../../BodyContentText.vue'
import TrollProfile from "./../../Trolls/Profile.vue"
import text from "./../../../assets/text.js"
import FakeRealImage from "./../../FakeRealImage.vue"
import Bar from './../../Charts/Bar.vue'
import createChartData from './../../Charts/createChartData'
import trollImageText from './../../../../public/troll.json'
import BarCustom from './../../Charts/BarCustom.vue'



export default {
  props: ["view"],
  components: {
    TrollProfileNavigation,
		BodyContentText,
		TrollProfile,
		FakeRealImage,
		Bar,
		trollImageText,
		BarCustom
  },
	data() {
		return {
			troll: {
				accountInfo: {
				}, 
			},
			images: {

			},
			charts: {
				replies: {},
				retweets: {},
				replies: {},
				hashtags: {}
			},
			text,
		}
	},
		methods: {
    onClickChild (value) {
			this.$data.images = trollImageText.filter((element) => element.troll.toLowerCase() === value.accountInfo.userName)
			this.$data.troll = value;
			this.$data.charts.retweets = createChartData(this.$data.troll, "retweets", 30, "retweets", 'rgb(249, 233, 111)','#f9e96f');
			this.$data.charts.replies = createChartData(this.$data.troll, "replies", 30, "Replies to user", 'rgb(92, 134, 74)','#5c864a');
			this.$data.charts.mentions = createChartData(this.$data.troll, "mentions", 30, "Mentioned user", 'rgb(90, 164, 214)','#5aa4d6');
			this.$data.charts.hashtags = createChartData(this.$data.troll, "hashtags", 30, "Used hashtags", 'rgb(234, 110, 51)','#ea6e33');

    },
		createChartData
  }
}
</script>

<style scoped>
@media only screen and (max-width: 768px) {
    .visualisations-group {
      width: 90vw;
      max-width: 1200px;
      min-width: 400px;
      height: 50vh;

    }
  }

  @media only screen and (min-width: 769px) {
    .visualisations-group {
      width: 45vw;
      max-width: 1200px;
      min-width: 500px;
      height: 50vh;
    }
  }
  .visualisations-container {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-wrap:  wrap 

  }
  .mikro-container {
		border-top: 1px solid #b0b0b0;
		border-bottom: 1px solid #b0b0b0;
    margin: auto 5%;
  }
	.image {
		width: 60vw;
		border: 3px solid #5aa4d6;
	}
	.visualisations {
    margin: 0 auto;
		width: 40vw;
		min-width: 300px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    overflow: hidden;
    background-color: "black";
  }
	.image-container {
		margin-top: 20px;
	}
	.url {
		/* Style for "Jordana Pa" */
		height: 15px;
		color: #000000;
		font-family: acumin-pro, sans-serif;
		font-size: 16px;
		font-weight: 700;
		font-style: normal;
		letter-spacing: normal;
		line-height: 16px;
		text-align: center;
		text-decoration: underline;
	}
  .visualisations canvas {
    flex-shrink: 0;
    width: 90%;
    height: 90%
}
</style>