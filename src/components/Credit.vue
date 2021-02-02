<template>
	<div class="container-banner">
		<p><slot></slot></p>
		<slot name="image"></slot>
	</div>
</template>

<style scoped>
	p {
		/* Style for "Projekt je" */
		color: #000000;
		font-family: acumin-pro, sans-serif;
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
	 @media only screen and (max-width: 768px) {
		.container-banner {
			width: 90vw;
			margin-top: 40px;
		}
	 }
	 @media only screen and (min-width: 769px) {
		.container-banner {
			width: 40vw;
			margin-top: 40px;
			height: 137px;
		}
	 }
</style>