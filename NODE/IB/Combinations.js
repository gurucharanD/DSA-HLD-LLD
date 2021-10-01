var data = [1, 2];
var count = 1
var subsets = []
var array = []

function print_subsets(str, sub, count, level) {
    if (level == str.length) {
        if (sub.length == 2 * count) {
            sub = sub.trim().split(' ')
            subsets.push(sub)
        }
        return subsets
    }
    print_subsets(str, sub + str[level] + ' ', count, level + 1);
    print_subsets(str, sub, count, level + 1);
}
print_subsets(data, '', count, 0)

console.log(subsets)