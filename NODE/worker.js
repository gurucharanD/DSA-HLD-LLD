var x = {
    Value: 0
};

function a(obj) {
    obj.Value++;
}

a(x);
console.log(x.Value);

f = function () {

    (() => {
        var a = 'a'
        let b = 'b'
    })()

    console.log(a, b)
}
f()

// a=[2,3,15,6]
// console.log(a.sort((a,b)=>{
// return b-a;
// }))
hiii
let i = Number.MIN_VALUE;
console.log(i)
console.log(i + 1)
console.log(i - 1)
console.log(i * i)
console.log(i / i)

console.log(3 < 2 < 1)
console.log(1 > 2 > 3)

a = [1, 2, 3] + [4, 5, 6]
console.log(typeof a)

b = [...[1, 2, 3], ...[4, 5, 6]]
console.log(b)

console.log(555555555555555555)
let j = Number.MAX_SAFE_INTEGER;
// console.log(j)


(function () {
    let a = b = 100
})()
console.log(a, b)

console.log(NaN === NaN)
// console.log(typeof NaN)



var i = 0;

function sum(n) {
    i += n;
    return sum;

}

sum(1)(2)(3)(6);
console.log(i);