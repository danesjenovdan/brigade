<template>
    <div @click="onClickButton" class="item">
			<div :class="clicked ? 'background' : null" >
				<profile-picture :src="imageUrl"></profile-picture>
				<p class="name" >{{name}}</p>
			</div>
    </div>
</template>

<script>
import ProfilePicture from './ProfilePicture.vue'
import text from '../assets/text.js'

  export default {
		components: {
			ProfilePicture
		},
		props: {
			imageUrl: { type: String },
			name: { type: String },
			id: { type: String },
			clicked: { type: Boolean },
		},
		methods: {
			onClickButton (event) {
				this.$emit('clicked', this.id)
			}
  	}
  }

</script>
<style scoped>
.background {
		background-image:url('/yellow-rectangle.png');
    background-position:center;
    background-repeat: no-repeat;
    background-size: 100%;
}
	.item {
    display: flex;
    flex-direction: column;
		justify-content: center;
		margin: 20px;
}
 .name {
	color: #000000;
	font-family: "acumin-pro", sans-serif;;
	font-size: 16px;
	font-weight: 500;
	font-style: normal;
	letter-spacing: normal;
	line-height: 16px;
	text-align: left;
 }
</style>