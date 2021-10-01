let n = 10;
let output = ''
for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (i + j >= n - 1) {
            output += '*'
        } else {
            output += ' '
        }
    }
    console.log(output)
    output = ''
}