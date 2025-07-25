const fs = require('fs');

const logData = (err, data) => {
	console.log(data)
}

fs.readFile('demo.txt', 'utf8', logData);
console.log("Reading...")