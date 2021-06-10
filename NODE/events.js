const events = require('events')

const eventEmitter = new events.EventEmitter()

eventEmitter.on('event1', () => {
    console.log('event 1 called')
})

eventEmitter.on('event2', () => {
    console.log('event 2  called')
})

setImmediate(() => {
    console.log('immediate');
});

setTimeout(() => {
    console.log('timeout');
}, 0);

process.nextTick(()=>{
    console.log('next tickl')
})



eventEmitter.emit('event1')
eventEmitter.emit('event2')