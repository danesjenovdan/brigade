<template>
    <div class="containter">
			<div class="imageContainer">
					<img class="image" alt="" :src="originalImage.imageUrl" />
          <img class="image" v-if="stolenImage" alt="" :src="stolenImage.imageUrl">
			</div>
			<div class="linkContainer">
				<div class="link">
					<img class="icon" alt="" src="/link.png" />
				 <a class="url" :href="stolenImage.sourceUrl">{{stolenImage.text}}</a>
				</div>
				<div v-if="originalImage" class="link">
					<img class="icon" alt="" src="/link.png" />
					<a class="url" :href="originalImage.sourceUrl">{{originalImage.text}}</a>
				</div>
			</div>
    </div>
</template>

<script>
export default {
	props: {
		originalImage: { type: Object, required: true },
		stolenImage: { type: Object }
	}
}
</script>

<style scoped>
	.container {
		display: flex; /* or inline-flex */
		flex-direction: column;
		width: 80vh;
	}
	.imageContainer {
		display: flex; /* or inline-flex */
		flex-direction: row;
		border: 3px solid #5aa4d6;
		width: 100%
	}
	.image {
		width: 40vw
	}
	.icon {
		width: 20px;
		height: 20px;
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
		justify-content: center;
	}
	.url {
		/* Style for "Jordana Pa" */
		width: 171px;
		height: 15px;
		color: #000000;
		font-family: "acumin-pro", sans-serif;
		font-size: 16px;
		font-weight: 700;
		font-style: normal;
		letter-spacing: normal;
		line-height: 16px;
		text-align: left;
		text-decoration: underline;
	}
</style>