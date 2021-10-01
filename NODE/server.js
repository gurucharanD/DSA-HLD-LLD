const http = require('https');
// const fs = require('fs');

// const options = {
//     key: fs.readFileSync('test/fixtures/keys/agent2-key.pem'),
//     cert: fs.readFileSync('test/fixtures/keys/agent2-cert.pem')
// };

// https.createServer(options, (req, res) => {
//     res.writeHead(200);
//     res.end('hello world\n');
// }).listen(8000);

console.log('hii')
http.createServer(function (req, res) {
    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.write('Hello World!');
    res.end();
}).listen(8080);