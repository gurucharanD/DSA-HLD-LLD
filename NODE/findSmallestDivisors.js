function findSmallestDivisors(s, t) {

    while (s.length <= t.length) {
        if (s == t) {
            const uniqChars = Array.from(new Set(t.split('')));
            return uniqChars.length
        }
        t += t;
    }
    return -1;
}

console.log(findSmallestDivisors('lrbb','lrbb'))