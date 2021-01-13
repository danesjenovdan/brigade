export default (info = {}, size = 30, label="") => {
	info = Object.entries(info);
	info.sort(function (a, b) {
		return b[1] - a[1];
	}).splice(size);
	const labels = [];
	const data = []
	info.forEach(element => {
		labels.push(element[0])
		data.push(element[1])
	});
	
	return {
    data: {
      labels,    
      dataset:
        { // another line graph
          label,
          data,
        }
    },
  }
}