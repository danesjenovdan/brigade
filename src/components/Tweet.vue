<template>
  <div>
		<blockquote class="twitter-tweet">
      <a :href="tweetUrl">
      </a>
    </blockquote>
    </div>
</template>
<script>
  import moment from 'moment'

  export default {
    props: [
      'tweetUrl',
    ],
    methods: {
        methodThatForcesUpdate() {
          // ...
          console.log("force update")
          this.$forceUpdate();  // Notice we have to use a $ here
          // ...
        }
    },
    watch: { 
      tweetUrl: async function(newVal, oldVal) { // watch it
          this.methodThatForcesUpdate()
        /*const headers = { 
          'Access-Control-Allow-Origin' : '*',
          'Access-Control-Allow-Methods' : 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        }
        const result = await axios(`https://publish.twitter.com/oembed?url=${newVal}`,{
          method: "GET", 
          headers: headers,
        })
        console.log('result: ', result);*/
        
        }
      }
  }
</script>