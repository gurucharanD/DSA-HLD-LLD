let n = 7;
for (let i = 0; i < n; i++) {
    let output = ''
    for (let j = 0; j < n; j++) {
        if (i === 0 || j === 0 || i === n - 1 || j === n - 1 || i === j || i + j === n - 1) {
            output += '*'
        } else {
            output += ' '
        }
    }
    console.log(output)
}