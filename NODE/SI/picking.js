function pickingNumbers(a) {
    return a.reduce((count, val) => {
            // count occurance of each number
            count[val]++
            // console.log(count, val, count[val])
            return count;
        }, new Array(100).fill(0))
        .reduce((max, val, index, count) => {
            console.log(max, val, index)
            // max number of integers such that the absolute 
            // difference between any two is 1
            if (max < val + count[index + 1]) {
                max = val + count[index + 1];
            }
            return max;
        }, 0);
}
console.log(pickingNumbers([4, 6, 5, 3, 3, 1]))