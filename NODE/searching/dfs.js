// let grades = [73, 67, 38, 33]
// let res = [];
// for (let i = 0; i < grades.length; i++) {
//     // console.log(grades[i], (5 - (grades[i] % 5)))

//     if (grades[i] >= 38 && (5 - (grades[i] % 5)) < 3) {
//         res.push(grades[i] + (5 - (grades[i] % 5)))
//     } else {
//         res.push(grades[i])
//     }
// }
// console.log(res)

// 'use strict';

// const fs = require('fs');

// process.stdin.resume();
// process.stdin.setEncoding('utf-8');

// let inputString = '';
// let currentLine = 0;

// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });

// process.stdin.on('end', _ => {
//     inputString = inputString.trim().split('\n').map(str => str.trim());

//     main();
// });

// function readLine() {
//     return inputString[currentLine++];
// }

// /*
//  * Complete the gradingStudents function below.
//  */
// function gradingStudents(grades) {
//     /*
//      * Write your code here.
//      */
//     let res = [];
//     for (let i = 0; i < grades.length; i++) {
//         if (grades[i] >= 38 && (5 - (grades[i] % 5)) < 3) {
//             res.push(grades[i] + (5 - (grades[i] % 5)))
//         } else {
//             res.push(grades[i])
//         }
//     }
//     return res;
// }

// function main() {
//     const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

//     const n = parseInt(readLine(), 10);

//     let grades = [];

//     for (let gradesItr = 0; gradesItr < n; gradesItr++) {
//         const gradesItem = parseInt(readLine(), 10);
//         grades.push(gradesItem);
//     }

//     let result = gradingStudents(grades);

//     ws.write(result.join("\n") + "\n");

//     ws.end();
// }

// function countApplesAndOranges(s, t, a, b, apples, oranges) {
//     let count = 0;
//     for (let i = 0; i < apples.length; i++) {
//         if ((a + apples[i]) >= s && (a + apples[i]) <= t) {
//             count++
//         }
//     }
//     console.log(count)
//     count = 0;
//     for (let i = 0; i < oranges.length; i++) {
//         if (b + oranges[i] >= s && b + oranges[i] <= t) {
//             count++
//         }
//     }
//     console.log(count)
// }

// countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
// 4523 8092 9419 8076
x1 = 4523
v1 = 8092
x2 = 9419
v2 = 8076
while (x2 >= x1) {
    if (x1 === x2) {
        console.log('YES')
    }
    x1 = x1 + v1;
    x2 = x2 + v2;
}