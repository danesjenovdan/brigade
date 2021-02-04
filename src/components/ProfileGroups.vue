<template>
	<div class="flex-grid">
    <profile
      id="profile"
      class="flex-grid-item"
      title="Lažni profili"
      subtitle="25 profilov"
      text="Skupina profilov, ki uporablja lažne profilne slike, širi politično propagando in za katere obstaja visoka verjetnost, da so lažni in del organizirane mreže (glej Mikro pogled)."
      imageUrl="/red.png">
    </profile>
    <profile
      id="profile"
      class="flex-grid-item"
      title="Brigada"
      subtitle="500 profilov"
      text="Skupina 500 profilov, ki sledi vsaj 5 od 27 profilov, za katere obstaja visoka verjetnost, da so lažni in del organizirane mreže (glej Mikro pogled)."
      imageUrl="/green.png">
    </profile>
    <profile
      id="profile"
      class="flex-grid-item"
      title="Politiki"
      subtitle="~90 profilov"
      text="Skupina profilov trenutno aktivnih politikov funkcionarjev: poslancev, ministrov, predsednikov strank in državnih sekretarjev."
      imageUrl="/blue.png">
    </profile>
		<profile
      id="profile"
      class="flex-grid-item"
      title="Kontrolni vzorec"
      subtitle="~150 profilov"
      text="Naključno izbran vzorec slovenskih uporabnikov omrežja Twitter. Vzorec smo sestavili tako, da smo teden dni snemali 1 % aktivnosti na Twitterju, filtrirali uporabnike, ki pišejo v slovenščini in iz njih sestavili vzorec."
      imageUrl="/yellow.png">
    </profile>
	</div >
</template>

<script>
import Profile from './Trolls/Profile.vue' // generilized component that can be used for troll type card
import text from '../assets/text.js'

export default {
  components: {
    Profile
  },
  data() {
    return text
  } 
}
</script>

<style scoped>
	.flex-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    margin-bottom: 100px;
  }
  	@media only screen and (max-width: 768px) {
    #profile {
      width: 80vw;
    }
  }
  .flex-grid-item {
    flex-grow: 0;
    flex-shrink: 0;
    margin-left: 25px;
		margin-right: 25px;
    margin-bottom: 10px;
    margin-top: 10px;
    align-items: center;
  }
</style>