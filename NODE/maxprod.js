let arr = [1, 2, 3, 4, 5]
let a = arr[0]
let b = arr[1]
let maxprod = a * b

for (let i = 1; i < arr.length - 1; i++) {
    prod = arr[i] * arr[i + 1]
    if (prod > maxprod) {
        maxprod = prod
        a = arr[i]
        b = arr[i + 1]
    }
}

console.log(a, b, maxprod)

// function shapeArea(n) {
//        return  (1 + (n-1)*n) *2 - 1;
//    }