var v = "guru"
// v = v.split("")
// console.log("v=>", v);
var p = []
var count = 0
for (var i = 0; i < v.length; i++) {
    if (v[i] > v[i + 1]) {
        dd(i);
        count++
        break;
    }
}

if (count === 0) {
    console.log("==> ", v.length - 1)
}



function dd(i) {
    console.log("==> ", i)
}



k = [1, 9, 30, 38]