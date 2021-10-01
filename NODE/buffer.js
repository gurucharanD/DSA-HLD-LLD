const fs = require('fs/promises')
const path = require('path')
const promise = fs.readFile(path.join('buffer.txt'));

Promise.resolve(promise).then(function (buffer) {
    console.log(buffer)
    fs.writeFile('./buffer.txt', buffer).then(console.log);
});