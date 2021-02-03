<template>
  <div class="container-text">
        <div class="title">
					<slot name="title"></slot>
				</div>
        <div class="text">
					<slot> </slot>
        </div>
  </div>
</template>

<style scoped>

@media only screen and (max-width: 768px) {
    .container-text {
      width: 80vw;
    }
  }

  @media only screen and (min-width: 769px) {
    .container-text {
        width: 60vw;
    }
  }

.container-text {
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
  display: flex; /* or inline-flex */
  flex-direction: column;
  justify-content: flex-start;
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
}
.text {
	color: #000000;
	font-family: acumin-pro, sans-serif;
	font-size: 20px;
	font-weight: 200;
	font-style: normal;
	letter-spacing: normal;
	line-height: 33.33px;
	text-align: left;
}
</style>

