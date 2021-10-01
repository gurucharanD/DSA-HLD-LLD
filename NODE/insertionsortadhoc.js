let a = [176, -272, -272, -45, 269, -327, -945, 176]

for (let i = 0; i < a.length; i++) {
    let sorted = a[i]
    for (let j = i + 1; j < a.length; j++) {
        if (a[j] < sorted) {
            temp = a[j + 1]
            a[j + 1] = a[j]
        }
    }
}