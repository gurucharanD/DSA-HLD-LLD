const {
    performance
} = require('perf_hooks');
let nemo = ['nemo']

function findNemo(array) {
    let t0 = performance.now();
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('foundNemo')
        }
    }
    let t1 = performance.now();
    console.log(t1 - t0)

}

findNemo(nemo)
const large = new Array(100).fill('guru', 1, 2);
console.log(large)