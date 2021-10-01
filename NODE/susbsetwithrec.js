var data = [1, 2, 1, -2]
var subsets = []

function print_subsets(str, sub, level) {
    if (level == data.length) {
        sub + (data[level]) + ' '
        subsets.push(sub)
        return;
    }
    print_subsets(str, sub + (data[level]) + ' ', level + 1);
    print_subsets(str, sub, level + 1);
}
print_subsets(data, '', 0);
console.log(subsets.sort())
// for (let i = 1; i < subsets.length; i++) {
//     let array = subsets[i].trim().split(' ')
//     let res = []
//     for (let j = 0; j < array.length; j++) {
//         res.push(Number(array[j]))
//     }
//     subsets[i] = res
// }
// console.log(subsets)

// subsets = subsets.sort((a, b) => a - b)
// console.log(subsets)
// let a =
//     [[3], [3, 5], [3, 15], [5], [3, 5, 15],]

// a = a.sort((a, b) => a - b)
// console.log(a)