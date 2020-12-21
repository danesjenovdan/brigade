<template>
    <img :src="url" alt=""/>
</template>

<script>
import SocialMediaIcon from './SocialMediaIcon.vue'
export default {
	components: {
		SocialMediaIcon
	},
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