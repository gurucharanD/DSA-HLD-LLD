// // var specialChars = "ab c!@#$^&%*()+guru=-[]\/{}|126:<huj>?,.";


// // var desired = specialChars.replace(/\s/g, '___').replace(/[^\w\s]/gi, '')
// // console.log(desired)


// let time = '12:05:05PM'
// time = time.split(':')
// time[0] = Number(time[0]) + 12
// if (time[0] >= 24) {
//     time[0] = 0
//     time[2] = time[2].substr(0, 2) + 'AM'
// }
// console.log(time[0] + ':' + time[1] + ':' + time[2])


// let a = new Set()
// // let b = [1, 2]

// // console.log(b instanceof Set)

// a.add(1)
// console.log(a)
// console.log(a.has(1))

function reverse(str) {
    let reversed = "";
    for (let char of str) {
        reversed = char + reversed;
        console.log(reversed);
    }
    return reversed;
}
console.log(reverse('abc'));