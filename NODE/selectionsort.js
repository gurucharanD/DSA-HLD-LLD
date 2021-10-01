// let a = [3, 4, 1, 8, 5, 2, 9, 0, 6, 7]
let a = [176, -272, -272, -45, 269, -327, -945, 176]
let index
let array = []
console.log(a)
for (let i = 0; i < a.length; i++) {
    let small = a[i]
    for (let j = i + 1; j < a.length; j++) {
        if (a[j] < small) {
            small = a[j]
            index = j
        }
        console.log(a)

    }
    temp = a[i]
    a[i] = small
    a[index] = temp
    array.push(index)
    // console.log(index)
}
console.log(a)
console.log(array)