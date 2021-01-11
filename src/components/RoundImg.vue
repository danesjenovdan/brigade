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
		margin-left:25px;
		margin-right: 25px;
		width: 68px;
		height: 68px;
   		border-radius: 50%;
	}
</style>