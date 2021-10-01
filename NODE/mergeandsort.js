let a = [1, 3, 6]
let b = [2, 4, 5]
let merge = []

let elem1 = a[0]
let elem2 = b[0]

let i = 1
let j = 1

while (elem1 || elem2) {
    console.log(elem1, elem2)
    if (!elem2 || elem1 < elem2) {
        merge.push(elem1);
        elem1 = a[i]
        i++
        console.log(merge)
    } else {
        merge.push(elem2);
        elem2 = b[j]
        j++
        console.log(merge)
    }
}

let merge2 = a.concat(b).sort()
console.log(merge2)

console.log(merge)