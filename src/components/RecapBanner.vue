<template>
	<div class="container-banner">
		<slot></slot>
	</div>
</template>

<style scoped>

	@media only screen and (max-width: 768px) {
		.container-banner {
			display: flex;
			justify-content: flex-start;
			align-items: center;
			height: 100%;
			width: 100%;
			padding-top: 30px;
			padding-bottom: 30px; 
		}
}

	@media only screen and (min-width: 769px) {
		.container-banner {
			width: 78vw;
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
		background-color: #f9e96f;
		margin-top: 150px;
	}
	img {
		width: 45%;
	}
	.facebook {
		width: 25%;
	}
</style>