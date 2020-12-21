<template>
	<div class="mikro-container">
    <profile-view></profile-view>
	</div>
</template>

<script>
import ProfileView from '../ProfileView.vue'

export default {
  props: ["view"],
  components: {
    ProfileView,
  },
}
</script>

<style scoped>
  .mikro-container {
		border-top: 1px solid #b0b0b0;
		border-bottom: 1px solid #b0b0b0;
    margin: auto 5%;
  }
</style>