const trollQuery = require('./ElasticQuery.js');

const arr = [
	"jocarules",
	"BostjanSeruga",
	"DesnicarkaM",
	"lenaradczik",
	"krek_janja",
	"lublanaCEE",
	"matevz007",
	"hanavrabec",
	"pusnikferdinand",
	"Medenakimi",
	"janez_novak",
	"ostanekatarina",
	"Banana81295013",
	"JureBregar",
	"1radovedna",
	"katarinamlakar",
	"karolinasemjaz",
	"ninalogar4",
	"Japelj62962",
	"punca9",
	"EvaResnik",
	"Kalofat",
	"luka_bizjak",
	"JERN3J",
	"jurzesky",
	"jan_gerben",
	"MajdaKravanja",
	"JanezR2"
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