<template>
	<div class="container-banner">
		<h1>Povej naprej!</h1>
		<div class="container-icons">
			<icon url="/facebook.png"/>
			<icon url="/twitter.png"/>
			<icon url="/mail.png"/>
		</div>
	</div>
</template>

<script>
import Icon from './Icon.vue'

  export default {
		components: {
			Icon
		}
  }

</script>
<style scoped>

	@media only screen and (max-width: 768px) {
		.container-banner {
			display: flex;
			justify-content: flex-start;
			flex-direction: column;
			align-items: center;
			height: 100%;
			width: 100%;
		}
}

	@media only screen and (min-width: 769px) {
		.container-banner {
			height: 166px;
		}
	}
			.container-icons {
			display: flex;
			justify-content: center;
			flex-direction: row;
		}
	h1 {
		/* Style for "POVEJ NAPR" */
		color: #000000;
		font-family: "buran_ussrregular";
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
		padding-left: 20px;
	}
	.container-banner {
		background-color: #f9e96f;
		margin-top: 150px;
	}
</style>