<template>
    <div class="containter">
			<div class="imageContainer">
				<slot></slot>
			</div>
			<div class="linkContainer">
				<div class="link">
					<img class="icon" alt="" src="/link.svg" />
					<slot name="original"></slot>
				</div>
				<div class="link">
					<img class="icon" alt="" src="/link.svg"/>
					<slot name="fake"></slot>
				</div>
			</div>
	</div>
</template>

<script>
export default {
}
</script>

<style scoped>
@media only screen and (max-width: 768px) {
	.link {
		justify-content: start;
	  }
  }

  @media only screen and (min-width: 769px) {
	  .link {
		justify-content: center;
	  }
  }
	.container {
		display: flex; /* or inline-flex */
		flex-direction: column;
		margin: 30px;
		background-color: red;
	}
	.icon {
		width: 20px;
		height: 20px;
		align-items: center;
	}
	.linkContainer {
		padding: 10px;
		display: flex; /* or inline-flex */
		flex-direction: row;
	}
	.link {
		display: flex;
		flex-direction: row;
		width: 100%;
		text-align: center;
		align-items: center;
	}
</style>