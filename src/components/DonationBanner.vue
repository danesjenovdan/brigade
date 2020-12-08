<template>
	<div class="container-banner">
		<p>Kampanjo smo na <span class="acumin">Danes je nov dan</span>
            pripravili v sodelovanju z <span class="acumin">Virostatiq</span>
    </p>
		<div class="donation-box">
			<p>Želiš podpreti naše delo?</p>
			<social-media-icon src="src/assets/facebook.png"/>
		<div>
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
    .acumin {
			font-family: "acumin-pro";
			font-weight: 700;
			font-style: normal;
			letter-spacing: normal;
			line-height: normal; 
    }
	p {
      color: #000000;
			font-family: "acumin-pro";
			font-size: 16px;
			font-weight: 400;
			font-style: normal;
			letter-spacing: normal;
			line-height: 20px;
			text-align: center;
	}
	.donation-box {
		display: flex;
    justify-content: center;
    flex-direction: row;
    align-items: center;
		margin: 50px;
	}
	.container-banner {
		background-color: #ea6e33;
    margin-top: 40px;
    height: 137px;
	}
</style>