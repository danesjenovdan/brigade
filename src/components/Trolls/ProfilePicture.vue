<template>
    <div @click="onClickButton" class="item">
			<div :class="clicked ? 'background' : 'no-background'" >
				<div class="image-container">
					<round-img :src="'/27TrolovProfilke/'+info.userName+'.jpg'"/>
					<span class="name">
					<p :class="clicked ? 'bold' : null" >{{displayedName}}</p>
						</span>
				</div>
			</div>
    </div>
</template>

<script>
import RoundImg from '../RoundImg.vue'
import text from '../../assets/text.js'

  export default {
		components: {
			RoundImg
		},
		props: {
			clicked: { type: Boolean },
			info: {type: Object},
		},
	data() {
		return {
			displayedName: ""
		}
	},
		methods: {
			onClickButton (event) {
				this.$emit('clicked', this.info)
			}
  	},
		mounted() {
			console.log(this.info.name)
			if(this.info.name.length > 13) {
				let name = this.info.name
				if (this.info.name.includes("#")) name = name.replace("#", " ")
				const splitName = name.split(' ')
				if (splitName.length === 3) this.$data.displayedName = splitName[0] + "\n"+splitName[1]+" " +splitName[2]
			  else if (splitName.length === 2) this.$data.displayedName = splitName[0] + "\n"+splitName[1]
				else this.$data.displayedName = splitName[0] + "\n"
			} else {
				this.$data.displayedName = this.info.name + "\n"
			}
 		}
  }

</script>
<style scoped>

.image-container {
	margin-top: 10px;
}
.background {
		background-image:url('/hover.svg');
    background-position:center;
    background-repeat: no-repeat;
    background-size: 111px 105px;
}
.no-background:hover {
		background-image:url('/hover.svg');
    background-position:center;
    background-repeat: no-repeat;
    background-size: 111px 105px;
}
	.item {
    display: flex;
    flex-direction: column;
		justify-content: center;
		margin: 20px;
		height: 111px;
	}
	.bold {
			font-weight: 700;
	}
 .name {
	color: #000000;
	font-family: acumin-pro, sans-serif;;
	font-size: 16px;
	font-weight: 500;
	font-style: normal;
	letter-spacing: normal;
	line-height: 16px;
	text-align: center;
	white-space: pre-wrap; 
 }
</style>