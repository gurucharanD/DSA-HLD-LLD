let a = [1, 3, 5, 7, 9]
let b = [2, 4, 6, 8]
let merge = []
let p1 = 0
let p2 = 0

while (p1 <= a.length && p2 < b.length) {
    if (a[p1] < b[p2]) {
        merge.push(a[p1])
        p1++
    } else {
        merge.push(b[p2])
        p2++
    }
}

while (p1 < a.length) {
    merge.push(a[p1])
    p1++
}
console.log(merge)