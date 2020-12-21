<template>
    <div class="item">
    	<profile-picture :src="imageUrl"></profile-picture>
			<p class="name" >{{name}}</p>
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
			id: { type: String }
		}
  }

</script>
<style scoped>
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