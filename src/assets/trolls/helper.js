fs = require('fs');

const arr = [
    //"jocarules",
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
	//"Banana81295013",
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

const func = async (screen_name) => {
      fs.readFile("./"+screen_name+"info.json", (err, data) => {
       const trollData = !err || err !== null ? JSON.parse(data) : {};
       trollData.accountInfo = {
           ...trollData.accountInfo,
           userName: screen_name,
        }
        console.log('rollData.accountInfo: ', trollData.accountInfo);
    fs.writeFile("./"+screen_name+"info"+".json", JSON.stringify(trollData), function (err) {
        console.log('write: ', screen_name);
        if (err) return console.log(err);
        return 0
    });
})
}


 (async () => {
   for (screen_name of arr) {
   screen_name = screen_name.toLowerCase()
   func(screen_name)
   }
 })()