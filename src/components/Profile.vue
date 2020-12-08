<template>
  <div class="container-group">
    <div class="head">
        <div class="left">
          <img alt="yellow circle" :src="`${imageUrl}`" />
        </div>
        <div class="right">
         <span class="title">{{title}}
          <h2>{{subtitle}}</h2>
        </div>
    </div>
    <div class="body">
`     {{text}}
   </div>
  </div>
</template>

<script>
  export default {
    props: {
      text: { type: String, required: true },
      title: { type: String, required: true },
      subtitle: { type: String, required: true },
      imageUrl: { type: String, required: true },
    },
  }

</script>

<style scoped>

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
.head {
  display: flex; /* or inline-flex */
  flex-direction: row;
  justify-content: flex-start;
  border-bottom: 1px solid;
  align-items: center;
  width: 100%;
  height: 20%;
  padding: 10px;

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
</style>

