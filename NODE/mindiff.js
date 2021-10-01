let A = [1, 4, 5, 8, 10]
let B = [6, 9, 15]
let C = [2, 3, 6, 6]

let diff = Infinity;
let i = 0;
let j = 0;
let k = 0;
let p = A.length;
let q = B.length;
let r = C.length;

while (i < p && j < q && k < r) {
    console.log(A[i], B[j], C[k])
    let maximum = Math.max(A[i], Math.max(B[j], C[k]));
    let minimum = Math.min(A[i], Math.min(B[j], C[k]));

    if (maximum - minimum < diff) {
        diff = maximum - minimum;
    }

    if (diff == 0)
        break;

    if (A[i] == minimum) {
        i++;
    }
    else if (B[j] == minimum) {
        j++;
    }
    else {
        k++;
    }
}

console.log(diff)