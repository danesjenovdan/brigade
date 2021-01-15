<template>
  <div class="container-view">
		<img class="image" alt="Vue logo" src="/Layer-top.png" />
		<div class="items">
			<div id="1" :class="show === 1? 'background' : null" >
				<p class="items-text"  @click="show = 1;goTo('makro')">
          <span :class="show === 1? 'spacing' : null">Makro pogled</span>
        </p>
			</div>
			<div id="2" :class="show === 2? 'background' : null">
				<p class="items-text" @click="show = 2;goTo('mikro')">
         <span :class="show === 2? 'spacing' : null">Mikro pogled</span>
        </p>
			</div>
			<div id="3" :class="show === 3? 'background' : null">
				<p class="items-text" @click="show = 3;goTo('prostorski')">
          <span :class="show === 2? 'spacing' : null">Prostorski pogled</span>
        </p>
			</div>
		</div>
		<img class="image" alt="Vue logo" src="/Layer-bottom.png" />
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
      background-image:url('/yellow-background.png');
      background-position:center;
      background-repeat: no-repeat;
  }
  .container-view {
    margin: 0 auto;
    margin-top: 90px;
    display: flex; /* or inline-flex */
    flex-direction: column;
    justify-content: center;
  }

  @media only screen and (max-width: 768px) {
    .items {
      margin: 0 auto;
      justify-content: center;
      overflow-x: auto;
      align-items: center;
      white-space: nowrap;
      width: 90vw;
      display: flex;
      flex-direction: column;
      
    }
    .background {
      background-size: 100%;
      letter-spacing: 6.4px;
    }
    .container-view { 
      width: 90vw;
    }
    .image {
      width: 80vw;
    }
  }

  @media only screen and (min-width: 769px) {
    .items {
      margin: 0 auto;
      width: 80vw;
      display: flex; /* or inline-flex */
      overflow-x:auto; 
      flex-direction: row;
      justify-content: space-evenly;
      white-space: nowrap;
    }
    .image {
      width: 80vw;
    }
    .background {
      background-size: 100%;
      letter-spacing: 6.4px;
    }
  }

  .spacing {
    letter-spacing: 6.4px
  }
  .items-text {
      /* Style for "Prostorski" */
      height: 23px;
      color: #000000;
      font-size: 34px;
      font-family: "buran_ussrregular";
      font-weight: 400;
      font-style: normal;
      letter-spacing: normal;
      text-align: left;
      /* Text style for "Prostorski" */
      font-style: normal;
      letter-spacing: 2.3px;
      line-height: normal;
      margin-left: 10px;
      margin-right: 10px;
      cursor: pointer;
  }

  .image {
    margin: 0 auto;
    z-index: 0;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    padding: 15px;
  }

</style>
