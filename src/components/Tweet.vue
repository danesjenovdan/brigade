<template>
  <div id="the-tweet"></div>
</template>
<script>
import * as TwitterWidgetsLoader from 'twitter-widgets';
  export default {
    props: [
      'tweetUrl',
    ],
    watch: { 
      tweetUrl: async function(newVal, oldVal) { // watch it
        document.getElementById('the-tweet').innerHTML = '';
        TwitterWidgetsLoader.load((err, twttr) => {
          twttr.widgets.createTweet(
            this.tweetUrl.split('/')[5],
            document.getElementById('the-tweet'),
            {
              align: 'middle'
            }
          );
        });
      }
    }
  }
</script>

<style scoped>
#the-tweet {
  width: 80%;
  max-width: 600px;
  margin: auto;
}
</style>