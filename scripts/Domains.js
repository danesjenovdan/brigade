const elasticsearch = require('elasticsearch');
const  { tall } = require('tall')
const client = new elasticsearch.Client({
  host: 'http://51.15.239.174:9200',
});

fs = require('fs');



(async() => {
    let allRecords = [];
    const domains = {};

// first we do a search, and specify a scroll timeout
var { _scroll_id, hits } = await client.search({
    index: 'tweets',
    scroll: '1000s',
    body: {
        query: {
            "regexp":{
                "urls": ".+"
            }
        },
        size: 10000,
        _source: true
    }
})
while(hits && hits.hits.length) {
    // Append all new hits
    for(const hit of hits.hits) {
        if (new Date(hit._source.pub_date) <= new Date('2019-10-01')) return // Filter out hits before 1. October 2019
        const url = hit._source.urls !== '' ? hit._source.urls.split(',') : null;
        for (const link of url) {
            try {
                let url = new URL(link)
                if(!domains[url.hostname]) { 
                    url = new URL(await tall(link));
                }
                if(domains[url.hostname]) domains[url.hostname] += 1;
                else domains[url.hostname] = 1;
              } catch (err) {
                console.error('Could not resolve hostname.', err);
              }
        }
    }
    allRecords.push(...hits.hits)

    console.log(`${allRecords.length} of ${hits.total.value}`)

    var { _scroll_id, hits } = await client.scroll({
        scrollId: _scroll_id,
        scroll: '1000s'
    })
}
fs.writeFile('domains.txt', JSON.stringify(domains), function (err) {
    if (err) return console.log(err);
    console.log('success');
  });
console.log(`Complete: ${allRecords.length} records retrieved`)
})()