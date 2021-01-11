<template>
	<div class="flex-grid">
		<group
      class="flex-grid-item"
      title="Kontrolni vzorec"
      subtitle="400 profilov"
      text="Naključno izbran vzorec slovenskih uporabnikov omrežja Twitter. Vzorec je bil izbran s pomočjo metode XXX"
      imageUrl="/yellow.png">
    </group>
    <group
      class="flex-grid-item"
      title="Brigada"
      subtitle="500 profilov"
      text="Skupina 500 profilov, ki sledi vsaj 6 od 27 profilov, za katere obstaja visoka verjetnost, da so lažni in del organizirane mreže (glej Mikro pogled)."
      imageUrl="/green.png">
    </group>
    <group
      class="flex-grid-item"
      title="Desničarji"
      subtitle="XX profilov"
      text="Skupina profilov, definiranih s pomočjo strojnega klasifikatorja, ki upošteva metapodatke profilov, povezanost profilov in vsebine njihovih objav ter jih na tej podlagi razvršča v pretežno desno politično opcijo."
      imageUrl="/red.png">
    </group>
    <group
      class="flex-grid-item"
      title="Levičarji"
      subtitle="Xxx profilov"
      text="Skupina profilov, definiranih s pomočjo strojnega klasifikatorja, ki upošteva metapodatke profilov, povezanost profilov in vsebine njihovih objav ter jih na tej podlagi razvršča v pretežno levo politično opcijo."
      imageUrl="/blue.png">
    </group>
	</div >
</template>

<script>
import Group from './Group.vue'
import text from './../assets/text.js'

export default {
  components: {
    Group
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