let a = [1, 2, 3, 4, 5, 6, 23, 333, 53, 765];
let key = 333;

let left = 0;
let right = a.length - 1;
while (left < right) {
    mid = Math.floor((left + right) / 2);
    if (a[mid] === key) {
        console.log(a[mid]);
        break;
    }
    if (key < a[mid]) {
        right = mid - 1
    }
    if (key > a[mid]) {
        left = mid
    }
}