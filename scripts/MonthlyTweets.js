const elasticsearch = require('elasticsearch');
const moment = require('moment')
const client = new elasticsearch.Client({
  host: 'http://51.15.239.174:9200',
});

(async () => {
	let startdate = "2019-09-30"
	const days = {}
	while (startdate !== "2021-12-01") {
		let from = 0
		const startDay = moment(startdate, "YYYY-MM-DD").add(1, 'days').format("YYYY-MM-DD");
		console.log('startDay: ', startDay);
		const currDay = moment(startdate, "YYYY-MM-DD").add(1, 'days').format("YYYY-MM")
		console.log('currDay: ', currDay);
		if(!days[currDay]) days[currDay] = 0;
		const EndDay = moment(startDay, "YYYY-MM-DD").add(2, 'days').format("YYYY-MM-DD");
		console.log('EndDay: ', EndDay);
		startdate = startDay;
		try {
			const response = await client.search({
				index: 'tweets',
				from: from,
				body: {
						query: {
							"query_string": {
								"query": `(text:*) AND (pub_date:{${startDay} TO ${EndDay}})`
								}
							},
							size: 1,
							"track_total_hits": true
						}	
					})
					days[currDay]+= response.hits.total.value;
		} catch (error) {
			console.log('error: ', error);
		}
	}
	console.log("count", days)
})()