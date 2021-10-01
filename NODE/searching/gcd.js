let a = 996510762,
    b = 605904;

while (b != 0) {
    let r = a % b;
    a = b;
    b = r;
}
console.log(a)