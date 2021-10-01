let n = Math.abs(961)
let low = 1
let high = n
while (low <= high) {
    mid = Math.floor((low + high) / 2)
    // console.log(mid)
    let res = (mid * mid)
    if (res == n) {
        console.log(mid)
    }
    if (res > n) {
        high = mid - 1
    } else {
        low = mid + 1
    }

}

// console.log(mid)