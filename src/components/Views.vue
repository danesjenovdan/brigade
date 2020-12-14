<template>
  <div class="container-view">
		<img class="image" alt="Vue logo" src="./../assets/Layer-top.png" />
		<div class="items">
			<div id="1" :class="show === 1? 'background' : null" >
				<p class="items-text"  @click="show = 1;goTo('makro')"> Makro pogled</p>
			</div>
			<div id="2" :class="show === 2? 'background' : null">
				<p class="items-text" @click="show = 2;goTo('mikro')">Mikro pogled</p>
			</div>
			<div id="3" :class="show === 3? 'background' : null">
				<p class="items-text" @click="show = 3;goTo('prostorski')">Prostorski pogled</p>
			</div>
		</div>
		<img class="image" alt="Vue logo" src="./../assets/Layer-bottom.png" />
  </div>
</template>
    <script> 
		export default {
		data(){
    	return {
					show: 1,
			}
			},
    methods: {
      goTo(route) {
        this.$router.push(route);
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

@media only screen and (max-width: 768px) {
  .items {
    margin: 0 auto;
    display: flex; /* or inline-flex */
    flex-direction: column;
    justify-content: center;
    align-items: center;
    white-space: nowrap;
  }
}

@media only screen and (min-width: 769px) {
  .items {
    margin: 0 auto;
    width: 80%;
    display: flex; /* or inline-flex */
    overflow-x:auto; 
    flex-direction: row;
    justify-content: space-evenly;
    white-space: nowrap;
  }
}

.items-text {
    /* Style for "Prostorski" */
    width: 184px;
    height: 23px;
    color: #000000;
    font-size: 23px;
    font-family: "buran_ussrregular";
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

.image {
  margin: 0 auto;
  width: 80%;
  z-index: 0;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  padding: 15px;
}

</style>
