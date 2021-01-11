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
    switch(type){
			case 'replies': 
				field = "in_reply_to_screen_name";
				regexp = { "in_reply_to_screen_name": ".+"}
				break;
			case 'hashtags': 
				field = "hashtags"
				regexp =  { "hashtags": ".+" }
				break;
			case 'retweets':
				field = "text"
				regexp =  { "text": "rt" }
				break;
			case 'mentions': {
				field = 'mentions'
				regexp =  { "mentions": ".+" }
				break;
			}
			default: 
				break;
    }

// first we do a search, and specify a scroll timeout
    const bool = {
		"filter": {
				regexp
			}
    }
		if(screen_name) bool.must ={ "term": { "screen_name": screen_name}};
		let { _scroll_id, hits } = await client.search({
				index: 'tweets',
				scroll: '1000s',
				body: {
						query: {
								bool,
						},
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
							const regex = RegExp(/(^RT @\w+:)/).exec(hits._source.text)
							if (regex === null) return
							obj = [regex[0].split(" ")[1].slice(0, -1)];
						} else {
							obj = hits._source[field].split(',')
						}
						console.log('obj: ', typeof obj);
			obj ? obj.forEach(key => {
				console.log('key: ', key);
				if(resource[key]) resource[key] += 1;
				else resource[key] = 1;
			}) : null
    })
    allRecords.push(...hits.hits);

    ({ _scroll_id, hits } = await client.scroll({
        scrollId: _scroll_id,
        scroll: '1000s'
    }))
}
fs.readFile("trolls/"+screen_name+".json", (err, data) => {
    const trollData = !err ? JSON.parse(data) : {};
    trollData[type] = resource;
    fs.writeFile("trolls/"+screen_name+".json", JSON.stringify(trollData), function (err) {
        if (err) return console.log(err);
        console.log('success');
    });
});
console.log(`Complete: ${allRecords.length} records retrieved`)
}