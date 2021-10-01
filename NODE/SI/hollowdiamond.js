let n = 11;
let mid = Math.floor(n / 2)
let output = ''
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (i + j === mid || i + j === (n - 1) + mid || j === i + mid || i === j + mid) {
            output += '*'
        } else {
            output += ' '
        }
    }
    console.log(output)
    output = ''
}