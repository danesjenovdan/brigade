<template>
  <div class="container-view">
		<img class="image" alt="Vue logo" src="./../assets/Layer-top.png" />
		<div class="items">
			<div id="1" :class="show === 1? 'background' : null" >
				<p class="items-text"  @click="show = 1"> Makro pogled</p>
			</div>
			<div id="2" :class="show === 2? 'background' : null">
				<p class="items-text" @click="show = 2">Mikro pogled</p>
			</div>
			<div id="3" :class="show === 3? 'background' : null">
				<p class="items-text" @click="show = 3">Prostorski pogled</p>
			</div>
		</div>
		<img class="image" alt="Vue logo" src="./../assets/Layer-bottom.png" />
  </div>
</template>


    <script> 
    //   background-image:url('./../assets/yellow-background.png');
		export default {
		data(){
    	return {
					show: 1,
			}
			}
		}
    </script>
<style scoped>
.background {
		background-image:url('./../assets/yellow-background.png');
    background-position:center;
    background-repeat: no-repeat;
    background-size: 100%;
}
.container-view {
  margin: 0 auto;
  margin-top: 90px;
  display: flex; /* or inline-flex */
  flex-direction: column;
  justify-content: center
}
.items {
  display: flex; /* or inline-flex */
  flex-direction: row;
  justify-content: space-evenly;
  white-space: nowrap;
  overflow: hidden;
}

.image {
  margin: 0 auto;
  width: 80%;
  z-index: 0;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  padding: 15px;
}

.items-text {
    /* Style for "Prostorski" */
    width: 184px;
    height: 23px;
    color: #000000;
    font-family: "Buran - USSR";
    font-size: 21px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 33.33px;
    text-align: left;
    /* Text style for "Prostorski" */
    font-style: normal;
    letter-spacing: 2.13px;
    line-height: normal;
}
</style>

