let input = 'datastructures'.split('')
// using set
let s = new Set();
let val = '.'
for (const iterator of input) {
    if (s.has(iterator)) {
        // console.log(iterator)
        // return iterator;
        val = iterator
    } else {
        s.add(iterator)
    }
}

// return undefined
console.log(val)




//naive solution

// for (let i = 0; i < input.length; i++) {
//     for (let j = 0; j < input.length; j++) {
//         if (input[i] === input[j] && i !== j) {
//             console.log(input[i])
//             return input[i]
//         }
//     }
// }