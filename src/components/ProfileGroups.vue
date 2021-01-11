<template>
	<div class="flex-grid">
		<profile
      class="flex-grid-item"
      title="Kontrolni vzorec"
      subtitle="400 profilov"
      text="Naključno izbran vzorec slovenskih uporabnikov omrežja Twitter. Vzorec je bil izbran s pomočjo metode XXX"
      imageUrl="/yellow.png">
    </profile>
    <profile
      class="flex-grid-item"
      title="Brigada"
      subtitle="500 profilov"
      text="Skupina 500 profilov, ki sledi vsaj 6 od 27 profilov, za katere obstaja visoka verjetnost, da so lažni in del organizirane mreže (glej Mikro pogled)."
      imageUrl="/green.png">
    </profile>
    <profile
      class="flex-grid-item"
      title="Desničarji"
      subtitle="XX profilov"
      text="Skupina profilov, definiranih s pomočjo strojnega klasifikatorja, ki upošteva metapodatke profilov, povezanost profilov in vsebine njihovih objav ter jih na tej podlagi razvršča v pretežno desno politično opcijo."
      imageUrl="/red.png">
    </profile>
    <profile
      class="flex-grid-item"
      title="Levičarji"
      subtitle="Xxx profilov"
      text="Skupina profilov, definiranih s pomočjo strojnega klasifikatorja, ki upošteva metapodatke profilov, povezanost profilov in vsebine njihovih objav ter jih na tej podlagi razvršča v pretežno levo politično opcijo."
      imageUrl="/blue.png">
    </profile>
	</div >
</template>

<script>
import Profile from './Trolls/Profile.vue' // generilized component that can be used for troll type card
import text from './../assets/text.js'

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
  }

  .flex-grid-item {
    flex-grow: 0;
    flex-shrink: 0;
    margin-left: 25px;
		margin-right: 25px;
    align-items: center;
  }
</style>