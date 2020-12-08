<template>
	<div class="container-banner">
		<h1>Povej naprej!</h1>
		<social-media-icon src="src/assets/facebook.png"/>
		<social-media-icon src="src/assets/twitter.png"/>
		<social-media-icon src="src/assets/mail.png"/>
	</div>
</template>

<script>
import SocialMediaIcon from './SocialMediaIcon.vue'

  export default {
		components: {
			SocialMediaIcon
		}
  }

</script>
<style scoped>
	h1 {
		/* Style for "POVEJ NAPR" */
		color: #000000;
		font-family: "Buran - USSR";
		font-size: 33px;
		font-weight: 400;
		font-style: normal;
		letter-spacing: normal;
		line-height: 24px;
		text-align: left;
		text-transform: uppercase;
		/* Text style for "POVEJ NAPR" */
		font-style: normal;
		letter-spacing: 6.67px;
		line-height: normal;
	}
	.container-banner {
		background-color: #f9e96f;
		margin-top: 150px;
		height: 166px;
	}
</style>