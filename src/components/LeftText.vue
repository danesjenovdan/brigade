<template>
  <div class="container-text">
        <div class="title">
					{{title}}
				</div>
        <div class="text">
					{{text}}
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
.title {
	color: #000000;
	font-family: "Acumin Pro - Black";
	font-size: 33px;
	font-weight: 400;
	font-style: normal;
	letter-spacing: normal;
	line-height: 40px;
	text-align: left;
	/* Text style for "Activity (" */
	font-style: normal;
	letter-spacing: normal;
	line-height: normal;
	margin-left: 40px;
	width: 70%;
}
.text {
	color: #000000;
	font-family: "Acumin Pro - Extra Light";
	font-size: 24px;
	font-weight: 400;
	font-style: normal;
	letter-spacing: normal;
	line-height: 33.33px;
	text-align: left;
	/* Text style for "Lorem ipsu" */
	font-style: normal;
	letter-spacing: normal;
	line-height: normal;
	margin-left: 40px;
		width: 70%;

}
</style>

