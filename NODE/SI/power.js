function power(a, b) {
    let pow = 1,
        x = a
    while (b > 0) {
        console.log(x, b)
        if (b & 1 == 1) {
            pow = pow * x
        }
        x = x * x
        b = b >> 1
    }
    return pow
}

console.log(typeof power(100, 100))