let a = [176, -272, -272, -45, 269, -327, -945, 176]
// let a = [-274, 161]
// let a = [274, 204, -161, 481, -606, -767, -351]
// let a = [154, -109]
// let a = [5, 3, 1, 5]
// let a = [40, 10, 20, 40]
let indexes = []
for (let i = a.length - 1; i >= 0; i--) {
    let max = a[i]
    let index;
    for (let j = i; j >= 0; j--) {
        if (a[j] >= max) {
            max = a[j];
            index = j;
        }
    }
    let temp = a[index]
    a[index] = a[i]
    a[i] = temp
    indexes.push(index)
}
// indexes.pop()
console.log(indexes)