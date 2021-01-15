const elasticsearch = require('elasticsearch');
fs = require('fs');



module.exports = async (screen_name, type) => {
	const client = new elasticsearch.Client({
		host: 'http://51.15.239.174:9200',
	});
	
	let allRecords = [];
    const resource = {};
		let regexp;
    let field; // which elastic search field we are looking for

		let query = {}
    switch(type){
			case 'replies': 
				field = "reply_to";
				query = {
					bool: {
						must: [
							{ "term": { "username": screen_name} },
					 { nested: {
							path: "reply_to",
							query: {
									"regexp":{
											"reply_to.name": ".+"
									}
							}
						}
						}
					]
				}
				}
				break;
			case 'hashtags': 
				field = "hashtags"
				query = {
					bool: {
						must: [
							{ "term": { "username": screen_name} },
							{ 	"regexp":{
								"hashtags": ".+"
						}}
						],
					},	
				}
				break;
			case 'retweets':
				field = "text"
				query = {
					bool: {
						must: [
							{ "term": { "username": screen_name} },
							{ "regexp":{
									"retweet": "true"
								}
							}
						],
					},
				}
				break;
			case 'mentions': {
				field = 'mentions'
				query = {
					bool: {
						must: [
							{ "term": { "username": screen_name} },
							{ nested: {
									path: "mentions",
									query: {
											"regexp":{
													"mentions.name": ".+"
											}
									}
							} }
						],
					},
				}
				break;
			}
			default: 
				break;
    }


		//if(screen_name) bool.must ={ "term": { "username": screen_name}};
		let { _scroll_id, hits } = await client.search({
				index: 'twint_politiki_tweets',
				scroll: '1000s',
				body: {
				query,
				size: 1000,
				_source: true
				}
		})
		while(hits && hits.hits.length) {
    // Append all new hits
    hits.hits.forEach(hits => {
			if (new Date(hits._source.pub_date) <= new Date('2019-10-01')) return // Filter out hits before 1. October 2019
			let obj;
			if (type === "retweets") {
							const regex = RegExp(/(^RT @\w+:)/).exec(hits._source.tweet)
							if (regex === null) return
							obj = [regex[0].split(" ")[1].slice(0, -1)];
						} else {
							obj = hits._source[field]
						}
						obj ? obj.forEach(key => {
							if( type === "hashtags") {
								if(resource[key]) resource[key] += 1;
								else resource[key] = 1;
							} else {
								if(resource[key.screen_name]) resource[key.screen_name] += 1;
								else resource[key.screen_name] = 1;
							}
						}) : null
    })
    allRecords.push(...hits.hits);

    ({ _scroll_id, hits } = await client.scroll({
        scrollId: _scroll_id,
        scroll: '1000s'
    }))
}
fs.readFile("politiki/"+screen_name+".json", (err, data) => {
		const trollData = !err ? JSON.parse(data) : {};
		trollData[type] = resource;
    fs.writeFile("politiki/"+screen_name+".json", JSON.stringify(trollData), function (err) {
        if (err) return console.log(err);
        console.log('success');
    });
});
console.log(`Complete: ${allRecords.length} records retrieved`)
}