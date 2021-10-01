let A = [1, 1, 2]
if (A.length == 0) {
    return A.length;
}

let k = 0;
for (let i = 1; i < A.length; i++) {
    if (A[k] != A[i]) {
        A[k + 1] = A[i];
        k++;
    }
}

console.log(k + 1);

