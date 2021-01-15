const fs = require('fs');
// First I want to read the file

myArgs = process.argv.slice(2);
console.log('myArgs[0]: ', myArgs[0]);
var text = fs.readFileSync(myArgs[0],'utf8')
const array = []
const obj = JSON.parse(text)
Object.keys(obj).forEach(key => {
    array.push({key: key, value: obj[key]})
})

array.sort((a, b) => b.value - a.value);
console.log('array: ', array);

const topX= []
array.slice([0], [myArgs[1]]).map((item, i) => {
    topX.push(item);
});
console.log('topX: ', topX.length);
console.log('topX: ', topX);

const labels = []
const values = []
topX.forEach(element => {
    labels.push(element.key)
    values.push(element.value)
})
console.log('labels: ', labels);
console.log('values: ', values);
fs.writeFile(myArgs[2], JSON.stringify({labels, values}), function (err) {
    if (err) return console.log(err);
    console.log('success');
  });