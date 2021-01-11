const trollQuery = require('./ElasticQueryTwints.js');

const arr = [
    'jozefhorvat'
];


(async () => {
	 for (troll of arr) {
		troll = troll.toLowerCase();
		await trollQuery(troll, 'replies');
		await trollQuery(troll, 'mentions')
		await trollQuery(troll, 'retweets')
		await trollQuery(troll, 'hashtags')
	}
})()