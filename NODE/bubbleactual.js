let a = [176, -272, -272, -45, 269, -327, -945, 176]
let count = 0
for (let i = 0; i < a.length - 1; i++) {
    for (let j = 0; j < a.length - 1; j++) {
        if (a[j] > a[j + 1]) {
            count++
            let c = a[j]
            a[j] = a[j + 1]
            a[j + 1] = c
        }
        // console.log(a)
    }
}

console.log(a)
console.log(count)

//if j=0 sorts in reverse