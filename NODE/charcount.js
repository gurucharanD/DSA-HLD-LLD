let a = 'hellllllllllo world'
let key = 'l'
a = a.split('')
let num = 1;
for (let i = 0; i < a.length; i++) {
    if (a[i] == key) {
        a[i] = num;
        num++
    }
}
// a.join('')
console.log(a.join(''))