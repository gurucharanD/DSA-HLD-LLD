const server = require('net').createServer();

server.on('connection', socket => {
    console.log('connected');
    socket.write('socket connected');
    socket.on('data', (data) => {
        console.log(data)
        socket.write(data)
    })
    socket.on('end', () => {
        console.log('end')
        socket.write('end')
    })
});

server.listen(8000, () => {
    console.log('server running');
})