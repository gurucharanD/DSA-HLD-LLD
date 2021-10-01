function substrings(string, k) {
    let substrings = []
    for (let i = 0; i <= string.length - k; i++) {
        substrings.push(string.substr(i, k))
    }
    console.log(substrings)
}

substrings('abcdefgh', 2)