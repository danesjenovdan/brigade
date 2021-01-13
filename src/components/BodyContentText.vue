<template>
  <div class="container-text">
        <div class="title">
					<slot name="title"> </slot>
				</div>
        <div class="text">
					<slot> </slot>
        </div>
  </div>
</template>

<script>
  export default {
    props: {
      text: { type: String },
      title: { type: String },
    },
  }

</script>

<style scoped>
.container-text {
  margin: 0 auto;
  margin-top: 70px;
  margin-bottom: 60px;
  display: flex; /* or inline-flex */
  flex-direction: column;
  justify-content: flex-start;
  width: 80vw;
}

.title {
	color: #000000;
	font-family: acumin-pro, sans-serif;
	font-size: 33px;
	font-weight: 900;
	font-style: normal;
	letter-spacing: normal;
	line-height: 40px;
	text-align: left;
	/* Text style for "Activity (" */
	font-style: normal;
	letter-spacing: normal;
	line-height: normal;
}
.text {
	color: #000000;
	font-family: acumin-pro, sans-serif;
	font-size: 24px;
	font-weight: 200;
	font-style: normal;
	letter-spacing: normal;
	line-height: 33.33px;
	text-align: left;
	/* Text style for "Lorem ipsu" */
	font-style: normal;
	letter-spacing: normal;
	line-height: normal;

}
</style>

