<template>
		<div class="flex-grid">
				<profile-picture @clicked="onClickChild" class="flex-grid-item"
				v-for="troll in trolls"
				:name="troll.accountInfo.name"
				:clicked = "troll.accountInfo.name === clickedName"
				:info = "troll.accountInfo"
				/>
		</div>
</template>

<script>
import ProfilePicture from './ProfilePicture.vue'
import desnicarkaminfo from '../../assets/trolls/desnicarkaminfo.json'
import karolinasemjazinfo from '../../assets/trolls/karolinasemjazinfo.json'
import radovednainfo from '../../assets/trolls/1radovednainfo.json'
import bostjanserugainfo from '../../assets/trolls/bostjanserugainfo.json'
import evaresnikinfo from '../../assets/trolls/evaresnikinfo.json'
import hanavrabecinfo from '../../assets/trolls/hanavrabecinfo.json'
import jan_gerbeninfo from '../../assets/trolls/jan_gerbeninfo.json'
import janez_novakinfo from '../../assets/trolls/janez_novakinfo.json'
import janezr2info from '../../assets/trolls/janezr2info.json'
import japelj62962info from '../../assets/trolls/japelj62962info.json'
import jern3jinfo from '../../assets/trolls/jern3jinfo.json'
import jurebregarinfo from '../../assets/trolls/jurebregarinfo.json'
import jurzeskyinfo from '../../assets/trolls/jurzeskyinfo.json'
import kalofatinfo from '../../assets/trolls/kalofatinfo.json'
import katarinamlakarinfo from '../../assets/trolls/katarinamlakarinfo.json'
import krek_janjainfo from '../../assets/trolls/krek_janjainfo.json'
import lenaradczikinfo from '../../assets/trolls/lenaradczikinfo.json'
import lublanaceeinfo from '../../assets/trolls/lublanaceeinfo.json'
import luka_bizjakinfo from '../../assets/trolls/luka_bizjakinfo.json'
import majdakravanjainfo from '../../assets/trolls/majdakravanjainfo.json'
import matevz007info from '../../assets/trolls/matevz007info.json'
import medenakimiinfo from '../../assets/trolls/medenakimiinfo.json'
import ninalogar4info from '../../assets/trolls/ninalogar4info.json'
import ostanekatarinainfo from '../../assets/trolls/ostanekatarinainfo.json'
import punca9info from '../../assets/trolls/punca9info.json'
import pusnikferdinandinfo from '../../assets/trolls/pusnikferdinandinfo.json'


export default {
  components: {
    ProfilePicture
  },
	data() {
		return {
			trolls: [
				desnicarkaminfo,
				karolinasemjazinfo,
				radovednainfo,
				bostjanserugainfo,
				evaresnikinfo,
				hanavrabecinfo,
				jan_gerbeninfo,
				janez_novakinfo,
				janezr2info,
				japelj62962info,
				jern3jinfo,
				jurebregarinfo,
				jurzeskyinfo,
				kalofatinfo,
				katarinamlakarinfo,
				krek_janjainfo,
				lenaradczikinfo,
				lublanaceeinfo,
				luka_bizjakinfo,
				majdakravanjainfo,
				matevz007info,
				medenakimiinfo,
				ninalogar4info,
				ostanekatarinainfo,
				punca9info,
				pusnikferdinandinfo,
			],
			clickedName: "White Right 🇸🇮"
		}
	},
	mounted() {
    	this.$emit('clicked', this.$data.trolls.find(element => element.accountInfo.name === this.$data.clickedName), this.$data.clickedName);
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
		cursor: pointer;
  }
}
</style>