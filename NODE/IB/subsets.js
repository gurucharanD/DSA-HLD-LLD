var subsets = []

function print_subsets(str, sub, level) {
    if (level == str.length) {
        sub + (str[level]) + ' '
        subsets.push(sub)
        return;
    }
    print_subsets(str, sub + (str[level]) + ' ', level + 1);
    print_subsets(str, sub, level + 1);
}

function letterCombinations(A) {
    var num1 = A.split('')[0]
    var num2 = A.split('')[1]
    var array = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    var data = array[num1].concat(array[num2])
    print_subsets(data, '', 0);
    return subsets
}
letterCombinations('23')
console.log(subsets)
