const http = require('http')
const port = 4200

const requestHandler = (request, response) => {
    console.log(request.url)
    response.end('Hello Node.js Server!')
}

// const server = http.createServer(requestHandler)

// server.listen(port, (err) => {
//     if (err) {
//         return console.log('something bad happened', err)
//     }

//     console.log(`server is listening on ${port}`)
// })

http.createServer(function (req, res) {
    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.write('Hello World!');
    res.end();
}).listen(8080);