<template>
    <img :src="url" alt=""/>
</template>

<script>
export default {
		props: {
			url: { type: String }
		}
}
</script>
<style scoped>
	img {
		margin-left: 15px;
		margin-right: 15px;
		width: 68px;
		height: 68px;
   		border-radius: 50%;
		margin-bottom: -15px;
	}
</style>