const fs = require('fs')
// fs.readFile('./bat.txt', (err, data) => {
//     console.log(data.toString())
// })
const csv = require('csv');
console.log(csv)
csv.generate
    .from(fs.createReadStream('./test.txt', {
        delimiter: ',',
        escape: ';'
    }))
    .to(fs.createWriteStream('./file.csv'))