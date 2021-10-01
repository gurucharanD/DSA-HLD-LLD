// const eventemitter = require('events');

// class sample extends eventemitter {
//     execute() {
//         this.emit('hello');
//     }
// }

// const ee = new sample()
// ee.on('hello', () => {
//     console.log('heloo sample');
// })

// ee.execute()

// function sample(cb, ...args) {
//     console.log(args.length)
//     cb();
// }

// sample(() => {
//     console.log('log');
// }, 'a', 'b')

function cb() {
    console.log('Processed in next iteration');
}
process.nextTick(cb);
console.log('Processed in the first iteration');