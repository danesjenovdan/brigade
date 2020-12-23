<template>
	<div class="container-banner">
		<p>Kampanjo smo na <span class="acumin"><a href="https://danesjenovdan.si/">Danes je nov dan</a></span>
            pripravili v sodelovanju z <span class="acumin"><a href="http://virostatiq.com/">Virostatiq</a></span>
    </p>
		<div class="donation-box">
			<p>Želiš podpreti naše delo?</p>
			<div class="rectangle">
				<span class="acumin"><a href="https://danesjenovdan.si/doniraj">Doniraj!</a></span>
				<img src="/heart.png" alt=""/>
			</div>
		</div>
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
	a {
  color: inherit; /* blue colors for links too */
  text-decoration: inherit; /* no underline */
	}
	img {
		width: 24px;
		height: 33ps;

	}
	.rectangle {
		        /* Style for "Rectangle" */
    width: 166px;
    height: 56px;
    border: 3px solid #000000;
    display: flex;
    justify-content: center;
    flex-direction: row;
    align-items: center;
    margin: 1rem;
	}
	.acumin {
		font-family: "acumin-pro", sans-serif;
		font-weight: 700;
		font-style: normal;
		letter-spacing: normal;
		line-height: normal; 
	}

	@media only screen and (max-width: 768px) {
   p {
		font-size: 12px;
	}
}

@media only screen and (min-width: 769px) {
  p {
		font-size: 16px;
	}
}
	p {
      color: #000000;
			font-family: "acumin-pro";
			font-weight: 400;
			font-style: normal;
			letter-spacing: normal;
			line-height: 1rem;
			text-align: center;
			padding: 1rem;
	}
	.donation-box {
		display: flex;
    justify-content: center;
    flex-direction: row;
    align-items: center;
		margin: 3rem;
	}
	.container-banner {
		background-color: #ea6e33;
    margin-top: 2.6rem;
    height: 137px;
	}
</style>