let array = [1, 2, 3]
let subsets = []
function sums(array, length, sum, subset, subsetsum, index) {
    console.log(sum, subsetsum, array[index], index, length)
    if (sum == subsetsum) {
        subsets.push(subset)
        sums(array, length, sum, subset, subsetsum - array[index], index + 1)
        return
    } else {
        for (let i = index; i < length; i++) {
            sums(array, length, sum, subset + ' ' + array[index], subsetsum + array[index], i + 1)
        }
    }
}

console.log(sums(array, array.length, 3, '', 0, 0))
console.log(subsets)