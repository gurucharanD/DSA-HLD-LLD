let cal = 0;
function factorial(n) {
    cal++;
    if (n == 0 || n == 1) {
        return n;
    }
    return n * factorial(n - 1)
}
console.log(factorial(10))
console.log(cal);