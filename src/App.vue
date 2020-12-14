<template>
  <div class="container">
    <img class ='header-image' alt="Vue logo" src="./assets/twitter-brigade.png" />
    <div class="container-body">
      <div class='body-text'>
       {{text}} {{text}} {{text}} {{text}} {{text}} {{text}}
      </div>
      <views/>
      <router-view></router-view>
      <social-media-banner/>
      <donation-banner/>
      <credit/>
    </div>
  </div>
</template>

<script>
  import Views from './components/Views.vue'
  import ProfileGroups from './components/ProfileGroups.vue'
  import text from './assets/text.js'
  import SocialMediaBanner from './components/SocialMediaBanner.vue'
  import DonationBanner from './components/DonationBanner.vue'
  import Credit from './components/Credit.vue'


  export default {
    name: 'App',
    components: {
      Views,
      ProfileGroups,
      SocialMediaBanner,
      DonationBanner,
      Credit
    },
    data() {
      return text
    }
  }
</script>

<style scoped>
  h1 {
    /* Style for "Activity (" */
    color: #000000;
    font-family: "acumin-pro", sans-serif;
    font-size: 33px;
    font-weight: 900;
    font-style: normal;
    letter-spacing: normal;
    text-align: left;
    /* Text style for "Activity (" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
    width: 70%;
  }
  .flex-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .flex-grid-item {
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: 13%;
    margin: 25px;
    display: flex;
    align-items: center;
  }

  .container {
    margin: 0 auto;
    display: flex; /* or inline-flex */
    flex-direction: column;
    justify-content: center;
    top: 0;
    position: absolute;
  }

  .container-body {
    display: flex; /* or inline-flex */
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 68px;
  }
  .header-image {
    width: 100%;
    z-index: 0;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    margin: 0;
  }

  .body-text {
    /* Style for "Lorem ipsu" */
    width: 50%;
    color: #000000;
    font-family: "acumin-pro", sans-serif;
    font-size: 24px;
    font-weight: 300;
    font-style: normal;
    letter-spacing: normal;
    line-height: 33.33px;
    text-align: left;
    /* Text style for "Lorem ipsu" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
    margin: 0 auto;
  }
</style>
