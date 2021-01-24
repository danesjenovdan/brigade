<template>
    <div @click="onClickButton" class="item">
			<div :class="clicked ? 'background' : 'no-background'" >
				<div class="image-container">
					<round-img :src="info.imageUrl"/>
					<span class="name">
					<p :class="clicked ? 'bold' : null" >{{info.name}}</p>
						</span>
				</div>
			</div>
    </div>
</template>

<script>
import RoundImg from './../RoundImg.vue'
import text from '../../assets/text.js'

  export default {
		components: {
			RoundImg
		},
		props: {
			clicked: { type: Boolean },
			info: {type: Object}
		},
		methods: {
			onClickButton (event) {
				this.$emit('clicked', this.info)
			}
  	}
  }

</script>
<style scoped>

.image-container {
	margin-top: 10px;
}
.background {
		background-image:url('/yellow-rectangle.png');
    background-position:center;
    background-repeat: no-repeat;
    background-size: 111px 105px;
}
.no-background:hover {
		background-image:url('/yellow-rectangle.png');
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
 }
</style>