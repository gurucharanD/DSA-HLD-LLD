array1 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

array2 = [
    [-44, 25, -52, 69, -5],
    [17, 22, 51, 27, -44],
    [-79, 28, -78, 1, -47],
    [65, -77, -14, -21, -6],
    [-96, 43, -21, -20, 90]
]
// 1 2 3
// 8 9 4
// 7 6 5u.k

function rotate(matrix) {
    const n = matrix.length;
    const x = Math.floor(n / 2);
    const y = n - 1;
    for (let i = 0; i < x; i++) {
        for (let j = i; j < y - i; j++) {
            console.log(i, j)
            k = matrix[i][j];
            matrix[i][j] = matrix[y - j][i];
            matrix[y - j][i] = matrix[y - i][y - j];
            matrix[y - i][y - j] = matrix[j][y - i]
            matrix[j][y - i] = k
        }
    }
}
// console.log(array2)
rotate(array1)
// console.log(array2)