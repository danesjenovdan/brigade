const fs = require('fs');
// First I want to read the file

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

arr.forEach(user => {
    const obj = fs.readFileSync('./trolls/'+user.toLowerCase()+'.json','utf8')
    let troll = JSON.parse(obj)
    const sorted = {}
    Object.keys(troll).forEach(key => {
        const tmp = Object.entries(troll[key]);
        tmp.sort(function (a, b) {
            return b[1] - a[1];
        }).splice(30);
        const labels = [];
        const data = []
        tmp.forEach(element => {
            labels.push(element[0])
            data.push(element[1])
        });
        troll[key] = tmp
    })
    
    console.log('sorted: ', troll);
    fs.writeFile('./trolls/chart30/'+user.toLowerCase()+'-chart30.json', JSON.stringify(troll), function (err) {
        if (err) return console.log(err);
        console.log('success');
      });
})