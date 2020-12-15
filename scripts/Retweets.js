const elasticsearch = require('elasticsearch');
const client = new elasticsearch.Client({
  host: 'http://51.15.239.174:9200',
});

fs = require('fs');


(async() => {
    let allRecords = [];
    const retweets = {};

// first we do a search, and specify a scroll timeout
var { _scroll_id, hits } = await client.search({
    index: 'tweets',
    scroll: '1000s',
    body: {
        query: {
            "regexp":{
                "text": "rt"
            }
        },
        size: 10000,
        _source: true
    }
})
while(hits && hits.hits.length) {
    // Append all new hits
    hits.hits.forEach(hits => {
        if (new Date(hits._source.pub_date) <= new Date('2019-10-01')) return // Filter out hits before 1. October 2019
       const regex = RegExp(/(^RT @\w+:)/).exec(hits._source.text)
       if (regex === null) return
       const retweet = regex[0].split(" ")[1].slice(0, -1); 
       if(retweets[retweet]) retweets[retweet] += 1;
       else retweets[retweet] = 1;

    })
    allRecords.push(...hits.hits)

    console.log(`${allRecords.length} of ${hits.total.value}`)

    var { _scroll_id, hits } = await client.scroll({
        scrollId: _scroll_id,
        scroll: '1000s'
    })
}
fs.writeFile('retweets.txt', JSON.stringify(retweets), function (err) {
    if (err) return console.log(err);
    console.log('success');
  });
console.log(`Complete: ${allRecords.length} records retrieved`)
})()