function interleave(s, t, res, i, j, array) {
    console.log(i, j, res)
    if (i == s.length && j == t.length) {
        array.push(res)
        return
    }
    if (i < s.length) {
        interleave(s, t, res + s[i], i + 1, j, array)
    }
    if (j < t.length) {
        interleave(s, t, res + t[j], i, j + 1, array)
    }
}

let res = []
interleave('ab', 'cd', '', 0, 0, res)
console.log(res)