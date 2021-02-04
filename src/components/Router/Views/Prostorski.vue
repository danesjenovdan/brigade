<template>
    <div class="visualisations-container">
        <network />
    </div>
</template>

<script>
import Network from '../../Charts/Network.vue';

export default {
  name: 'Prostorski',
  components: { Network }  
};
</script>

<style scoped>
.visualisations-container {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-wrap:  wrap ;
    width: 80vw;
  }
</style>