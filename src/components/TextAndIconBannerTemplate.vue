<template>
	<div class="container-banner">
		<slot name="text"></slot>
		<slot></slot>
	</div>
</template>

<style scoped>

	@media only screen and (max-width: 768px) {
		.container-banner {
			display: flex;
			justify-content: flex-start;
			flex-direction: column;
			align-items: center;
			height: 100%;
			width: 100%;
			padding-top: 30px;
			padding-bottom: 30px; 
		}
}

	@media only screen and (min-width: 769px) {
		.container-banner {
			height: 166px;
			width: 38vw;
            padding-top: 30px;
			padding-bottom: 30px; 
			flex-direction: column;
			justify-content: space-evenly;
			}
		}
		.container-icons {
			display: flex;
			justify-content: space;
			flex-direction: row;
			cursor: pointer;
		}

	.container-banner {
		background-color: #ea6e33;
		margin-top: 35px;
	}
	img {
		width: 45%;
	}
	.facebook {
		width: 25%;
	}
</style>