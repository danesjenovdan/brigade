<template>
	<div>
    <slot></slot>
	</div>
</template>

<script>
  export default {
    props: {
      url: { type: String, required: true },
    },
  }

</script>

<style scoped>
  div {
        /* Style for "Rectangle" */
    width: 78px;
    height: 78px;
    border: 3px solid #000000;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin: 15px;
  }
</style>