<template>
	<div class="container-banner">
        Projekt je nastal s podporo
    </p>
	<img src="./../assets/acf.png" alt=""/>
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
	p {
		/* Style for "Projekt je" */
		color: #000000;
		font-family: "acumin-pro";
		font-size: 12px;
		font-weight: 400;
		font-style: normal;
		letter-spacing: normal;
		text-align: left;
		/* Text style for "Projekt je" */
		font-style: normal;
		letter-spacing: normal;
		line-height: normal;
	}
	img {
		/* Style for "Active-cit" */
		width: 141px;
		height: 49px;
		margin: 50px
	}
	.container-banner {
    margin-top: 40px;
    height: 137px;
	}
</style>