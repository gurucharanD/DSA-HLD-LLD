let list = []
function fibo(n) {
    if (n < 2) {
        return n;
    }
    let res = fibo(n - 1) + fibo(n - 2);
    list.push(res);
    return list;
}
console.log(fibo(5))

// function fibo(n){
//     let a=0;
//     let b=

// }