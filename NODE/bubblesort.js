let a = [1, 49, 5, 88, 5443434, 24, 38]

for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a.length; j++) {
        if (a[i] > a[j]) {
            let c = a[j]
            a[j] = a[i]
            a[i] = c
        }
        // console.log(a)
    }
}

console.log(a)

//if j=0 sorts in reverse


for (let i = 0; i < a.length - 1; i++) {
    for (let j = 0; j < a.length - 1; j++) {
        if (Number(a[j]) > Number(a[j + 1])) {
            count++
            let c = a[j]
            a[j] = a[j + 1]
            a[j + 1] = c
        }
    }

}