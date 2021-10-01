
let a = [176, -272, -272, -45, 269, -327, -945, 176]


for (let i = 1; i < a.length; i++) {
    let key = a[i]
    let j = i - 1;
    while (j >= 0 && a[j] > key) {
        console.log(key, a[j + 1], a[j])
        a[j + 1] = a[j]
        j = j - 1
        // this loop shifts all the elements to right to create position for unsorted element
    }
    a[j + 1] = key;
    console.log(a)
    //this inserts unsorted element into its correct position
}
console.log(a)