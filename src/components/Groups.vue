<template>
  <div class="container-group">
    <div class="head">
        <div class="left">
          <img v-if="text" alt="" :src="imageUrl" />
          <img v-else alt="" class="userImage" :src="info.imageUrl">
        </div>
        <div v-if="text" class="right">
         <span class="title">{{title}}</span>
          <h2>{{subtitle}}</h2>
        </div>
        <div v-else class="right">
          <span class="profileName">{{info.name}}</span>
        </div>
    </div>
    <div v-if="text" class="body">
      {{text}}
   </div>
   <div v-else class="user-body">
        Lokacija: <b><i> {{info.location}}</i></b>
        <div class="line"/>
        Št. sledilcev: <b><i> {{info.nfollowers}}</i></b>
        <div class="line"/>
        Št. sledenih: <b><i> {{info.nFollowing}}</i></b>
        <div class="line"/>
        Št. tvitov: <b><i> {{info.nTweets}}</i></b>
        <div class="line"/>
        Datum registracije: <b><i> {{info.registrationDate}}</i></b>
   </div>
  </div>
</template>
<script>
  export default {
    props: {
      text: { type: String },
      info: { type: Object },
      title: { type: String, required: true },
      subtitle: { type: String, required: true },
      imageUrl: { type: String, required: true },
    },
  }
</script>

<style scoped>
  .line {
    border-bottom: 1px solid #b0b0b0;
    height: 1px;
    margin-bottom: 3px;
    margin-top: 5px;
  }
  .container-group {
    margin: 10px auto;
    display: flex; /* or inline-flex */
    flex-direction: column;
    justify-content: center;
    border: 1px solid;
    padding: 10px;
  }
  .body {
    margin: 25px;
    padding: 5px;
    width: 225px;
    text-align: left;
  }
  .user-body {
    padding: 5px;
    width: 225px;
    text-align: left;
  }
  .head {
    display: flex; /* or inline-flex */
    flex-direction: row;
    justify-content: flex-start;
    border-bottom: 1px solid;
    align-items: center;
    width: 100%;
    height: 20%;

  }
  .left {
    margin: 5px;
    /* Style for "Layer 32" */
  }
  .right {
    margin: 10px;
    white-space: nowrap;
  }
  img {
    /* Style for "Layer 32" */
    width: 39px;
    height: 41px;
    object-fit: cover;
  }
  .userImage {
    width: 68px;
    height: 68px;
    object-fit: cover;
    border-radius: 50%;
  }
  p {
    /* Style for "Lorem ipsu" */
    color: #000000;
    font-family: "acumin-pro", sans-serif;
    font-size: 12px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 16px;
    text-align: left;
    /* Text style for "L, orem ip" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
  h2 {
    /* Style for "400 profil" */
    width: 65px;
    height: 11px;
    color: #000000;
    font-family: "acumin-pro", sans-serif;
    font-size: 12px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 16px;
    text-align: left;
    /* Text style for "400 profil" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
  .title {
    /* Style for "Kontrolni" */
    width: 72px;
    height: 28px;
    color: #000000;
    font-family: "acumin-pro", sans-serif;
    font-size: 16px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 16px;
    text-align: left;
    /* Text style for "K, ontroln" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
  .profileName {
    width: 72px;
    color: #000000;
    font-family: "acumin-pro", sans-serif;
    font-size: 16px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 16px;
    text-align: left;
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
</style>

