function f(str, n, index, open, close) {
    if (index == 2 * n - 1) {
        str = str.trim();
        console.log(str)
        return
    }
    if (open < n / 2) {
        str = str + '('
        f(str, n, index + 1, open + 1, close)
    }
    if (close < n / 2) {
        str = str + ')'
        f(str, n, index + 1, open, close + 1)
    }
}
f('', 1, 0, 0, 0)
