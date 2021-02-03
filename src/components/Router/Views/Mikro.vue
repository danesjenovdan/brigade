<template>
  <body-content-text>
    <p>Predstavljamo Twitter profile, za katere obstaja močan indic, da so del organizirane propagandne mreže lažne javnosti. Namen uporabe lažnih profilnih slik, imen, opisov in celo posameznih tvitov je ustvarjanje vtisa avtentičnosti, ki je ključnega pomena za učinkovitost astroturfinga. Bolj kot profil izgleda avtentičen, bolj kredibilno lahko izpade njegovo mnenje. </p>
    <p>Predstavljeni profili so zgolj primeri takšnih, za katere je neavtentično delovanje najbolj očitno. 
Spodnje analize nam služijo kot vpogled v različne oblike in metode astroturfinga. Nekateri profili uporabljajo ukradeno identiteto, drugi celo strojno zgenerirane fotografije. Nekateri profili so namenjeni ustvarjanju vsebine, drugi osredotočeni bolj na všečkanje in ritvitanje.</p>
		<p>Glede na to, da lahko podobno vsebino in aktivnost opazimo tudi pri mnogo drugih Twitter profilih, lahko sklepamo, da je dejansko število neavtentičnih profilov precej večje. Žal pa je zaradi pomanjkanja trdnih dokazov, ne moremo razkriti. To moč ima zgolj podjetje Twitter.</p>
  </body-content-text>
	<div class="mikro-container">
		<troll-profile-navigation @clicked="onClickChild"/>
	</div>
	<div class="profile-container">
		<troll-profile v-if="troll.accountInfo.name" :info="troll.accountInfo"/>
	</div>
	<body-content-text>{{description}}</body-content-text>
	<fake-real-image class="image-container" v-for="image in images">
		<img class="image" alt="" :src="'/27Trolov' + image.src" />
			<template v-slot:original>
					<i v-if="image.src.includes('/desnicarkaM-1.jpg')">
					<a target="_blank" class="url" :href="image.leftLink.split(',')[0]">{{image.leftCaption.split(',')[0]}},<br/></a>
					<a target="_blank" class="url" :href="image.leftLink.split(',')[1]">{{image.leftCaption.split(',')[1]}},<br/></a>
					<a target="_blank" class="url" :href="image.leftLink.split(',')[2]">{{image.leftCaption.split(',')[2]}}<br/></a>
					</i>
					<i v-else><a target="_blank" class="url" :href="image.leftLink">{{image.leftCaption}}</a></i>
		</template>
		<template v-slot:fake>
				<i><a target="_blank" class="url" :href="image.rightLink">{{image.rightCaption}}</a></i>
		</template>
	</fake-real-image>
	<body-content-text>
			<template v-slot:title>
				Top tvit
			</template>
		</body-content-text>
		<div id="tweet" tweetID="515490786800963584"></div>
			<blockquote class="twitter-tweet" data-dnt="true" data-theme="light"><a :href="tweet[0] ? tweet[0].LINK : null"></a></blockquote>
		<body-content-text>
		<template v-slot:title>
			Top lestvice
		</template>
	</body-content-text>
	<div v-if="troll.accountInfo.name && troll.mentions" class="visualisations-container">
		<div class="visualisations-group"><bar-custom :data="charts.retweets" borderColor='rgb(249, 233, 111)'
					fillColor='#f9e96f' id="retweets"/></div>
			<div class="visualisations-group"><bar-custom :data="charts.mentions" borderColor='rgb(90, 164, 214)'
				fillColor='#5aa4d6' id="mentions"/></div>
			<div class="visualisations-group"><bar-custom :data="charts.domains" borderColor='rgb(234, 110, 51)'
					fillColor='#ea6e33' id="domains"/></div>
			<div class="visualisations-group"><bar-custom :data="charts.hashtags" borderColor='rgb(92, 134, 74)'
				fillColor='#5c864a' id="hashtags"/></div>
	</div>
	<div v-else class="visualisations-container">
		<body-content-text>Brez podatkov za leto 2020</body-content-text>
	</div>

</template>

<script>
import TrollProfileNavigation from '../../Trolls/ProfileNavigation.vue'
import BodyContentText from '../../BodyContentText.vue'
import TrollProfile from "./../../Trolls/Profile.vue"
import text from "./../../../assets/text.js"
import FakeRealImage from "./../../FakeRealImage.vue"
import Bar from '../../Charts/Bar.vue'
import createChartData from '../../Charts/createChartData'
import trollImageText from '../../../../public/troll.json'
// import tweets from '../../../../public/tweets.json'
import BarCustom from '../../Charts/BarCustom.vue'



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
			tweet: {
			},
			description: "",
			charts: {
				replies: {},
				retweets: {},
				domains: {},
				hashtags: {}
			},
			text,
		}
	},
		methods: {
    onClickChild (value) {
			this.$data.images = trollImageText.filter((element) => element.troll.toLowerCase().replace('@', '') === value.accountInfo.userName.toLowerCase().replace('@', ''))
			this.$data.description = trollImageText.find((element) => element.troll.toLowerCase().replace('@', '') === value.accountInfo.userName.toLowerCase().replace('@', '')).description
			this.$data.troll = value;
			this.$data.charts.retweets = createChartData(this.$data.troll, "retweets", 30, "RT", 'rgb(249, 233, 111)','#f9e96f');
			this.$data.charts.domains = createChartData(this.$data.troll, "domains", 30, "Domene", 'rgb(92, 134, 74)','#5c864a');
			this.$data.charts.mentions = createChartData(this.$data.troll, "mentions", 30, "Omembe", 'rgb(90, 164, 214)','#5aa4d6');
			this.$data.charts.hashtags = createChartData(this.$data.troll, "hashtags", 30, "Ključniki", 'rgb(234, 110, 51)','#ea6e33');

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
      height: 60vh;	
    }
		.url {
			font-size: 14px;
		}
  }

  @media only screen and (min-width: 769px) {
    .visualisations-group {
      width: 35vw;
      max-width: 1200px;
      min-width: 500px;
      height: 60vh;
    }
		.url {
			font-size: 16px;
		}
  }
	.tweet {
		display:flex;
		align-items: left;
		justify-content:center;
		width: 50vw;

	}
  .visualisations-container {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-wrap:  wrap ;
    width: 80vw;
		margin-top: 20px;
  }
	.profile-container {
    display: flex;
    justify-content: left;
    align-items: center;
    overflow: hidden;
    flex-wrap:  wrap ;
    width: 80vw;
		margin-top: 20px;
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