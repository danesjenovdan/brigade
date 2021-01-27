<template>
    <div class="containter">
			<div class="imageContainer">
				<slot></slot>
			</div>
			<div class="linkContainer">
				<div class="link">
					<img class="icon" alt="" src="/link.png" />
					<slot name="original"></slot>
				</div>
				<div class="link">
					<img class="icon" alt="" src="/link.png"/>
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
	.container {
		display: flex; /* or inline-flex */
		flex-direction: column;
		margin: 30px;
		background-color: red;
	}
	.icon {
		width: 20px;
		height: 20px;
		margin-right: 5px;
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
		justify-content: center;
	}
</style>