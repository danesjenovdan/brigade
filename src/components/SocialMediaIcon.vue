<template>
	<div>
    <img :src="`${src}`" alt=""/>
	</div>
</template>

<script>
  export default {
    props: {
      src: { type: String, required: true },
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
    margin: 20px;
  }

  img {
/* Style for "facebook" */
    width: 27px;
    height: 33px;
  }
</style>