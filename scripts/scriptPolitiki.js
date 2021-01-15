const trollQuery = require('./ElasticQueryTwints.js');

(async () => {
       await trollQuery("*", 'replies');
       await trollQuery("*", 'mentions')
       await trollQuery("*", 'retweets')
       await trollQuery("*", 'hashtags')
})()