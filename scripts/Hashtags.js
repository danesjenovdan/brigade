const elasticsearch = require('elasticsearch');
const client = new elasticsearch.Client({
  host: 'http://51.15.239.174:9200',
});

fs = require('fs');



(async() => {
    let allRecords = [];
    const hashtags = {};

// first we do a search, and specify a scroll timeout
var { _scroll_id, hits } = await client.search({
    index: 'tweets',
    scroll: '1000s',
    body: {
        query: {
            "regexp":{
                "hashtags": ".+"
            }
        },
        size: 10000,
        _source: true
    }
})
while(hits && hits.hits.length) {
    // Append all new hits
    hits.hits.forEach(hits => {
        if (new Date(hits._source.pub_date) <= new Date('2019-10-01')) return // Filter out
        const hashtag = hits._source.hashtags !== '' ? hits._source.hashtags.split(',') : null;
        hashtag ? hashtag.forEach(hash => {
           if(hashtags[hash]) hashtags[hash] += 1;
           else hashtags[hash] = 1;
        }) : null
    })
    allRecords.push(...hits.hits)

    console.log(`${allRecords.length} of ${hits.total.value}`)

    var { _scroll_id, hits } = await client.scroll({
        scrollId: _scroll_id,
        scroll: '1000s'
    })
}
fs.writeFile('hashtags.txt', JSON.stringify(hashtags), function (err) {
    if (err) return console.log(err);
    console.log('Hashtags.txt');
  });
console.log(`Complete: ${allRecords.length} records retrieved`)
})()