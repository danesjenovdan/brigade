<template>
  <div class="container-view">
		<img class="image" alt="Vue logo" src="/Layer-top.png" />
		<div class="items">
        <div class="container-description">
          <div id="mikro" :class="show.includes('mikro') ? 'background' : 'no-background'">
            <p class="title" @click="goTo('mikro')">
            <span :class="show.includes('mikro') ? 'spacing' : null">Mikro pogled</span>
            </p>
            </div>
          <div class="subtitle">
            <p>Analize 25 profilov, za katere obstaja <br/>visoka verjetnost, da so lažni in del <br/>organizirane mreže</p>
            </div>
        </div>
      <div class="container-description">
        <div id="makro" :class="show.includes('makro') ? 'background' : 'no-background'" >
          <p class="title"  @click="goTo('makro')">
            <span :class="show.includes('makro') ? 'spacing' : null">Makro pogled</span>
          </p>
        </div>
        <div class="subtitle">
          <p>Analize 4 različnih skupin Twitter uporabnikov, <br/>ki jih je mogoče primerjati med sabo.</p>
        </div>
        </div>
        <div class="container-description">
          <div id="prostorski" :class="show.includes('prostorski') ? 'background' : 'no-background'">
            <p class="title" @click="goTo('prostorski')">
              <span :class="show.includes('prostorski') ? 'spacing' : null">Prostorski pogled</span>
            </p>
          </div>
        <div class="subtitle">
          <p>Vizualizacija uporabnikov Twitter omrežja<br/>
          razporejenih s pomočjo strojnega klasifikatorja,<br/> ki upošteva vsebine meta podatke profilov,<br/> povezanost profilov in vsebine njihovih objav.</p>
        </div>
        </div>
		</div>
		<img class="image" alt="Vue logo" src="/Layer-bottom.png" />
  </div>
</template>

<script> 
export default {
  data() {
    return {
      show: 'mikro',
    }
  },
  mounted() {
    this.show = document.location.href.split('/')[3];
  },
  methods: {
    goTo(route) {
      this.show = route;
      this.$router.push(route);
    }
  },
};
</script>
<style scoped>
  .background {
      background-image:url('/yellow-background.png');
      background-position:center;
      background-repeat: no-repeat;
  }
  .no-background:hover {
      background-image:url('/yellow-background.png');
      background-position: center;
      background-repeat: no-repeat;
  }
  .container-view {
    margin: 0 auto;
    margin-top: 90px;
    display: flex; /* or inline-flex */
    flex-direction: column;
    justify-content: center;
  }
  .container-description {
    display: flex;
    flex-direction: column;
    margin: 20px;
  }

  .subtitle {
    color: #000000;
	  font-family: acumin-pro, sans-serif;
    flex-wrap: wrap;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    text-align: center;
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
    .subtitle {
      font-size: 16px;
    }
    .title {
      font-size: 32px;
    }
    .background {
      background-size: 100%;
      letter-spacing: 6.4px;
    }
    .no-background {
      background-size: 100%;
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
    .subtitle {
      font-size: 1vw;
      margin-top: -20px;
    }
    .title {
      font-size: 1.9vw;
    }
    .image {
      width: 80vw;
    }
    .background {
      background-size: 100%;
      letter-spacing: 6.4px;
    }
    .no-background {
      background-size: 100%;
    }
  }

  .spacing {
    letter-spacing: 6.4px
  }
  .title {
      /* Style for "Prostorski" */
      height: 23px;
      color: #000000;
      font-family: "buran_ussrregular";
      font-weight: 400;
      font-style: normal;
      letter-spacing: normal;
      text-align: center;
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
  .invisible {
    color:white;
  }
</style>
