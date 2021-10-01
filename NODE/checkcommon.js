let a = ['a', 'b', 'c'];
let b = ['d', 'e', 'f'];
let map = {};

a.map(element => {
    if (!map[element]) {
        map[element] = true;
    }
})
console.log(a)
b.forEach(element => {
    if (map[element]) {
        console.log(true);
    }
});
// console.log(x)
// const arr = [
//     ['name', 'Bob'],
//     ['age', 42],
//     ['breakfast', 'eggs']
// ];

// const mp = new Map(arr);

// // Get one particular value:
// console.log(mp.get('age'));
// // Get all the keys:
// console.log(...mp.keys());
// // Get all the values:
// console.log(...mp.values());
// // Get all the key/value pairs:
// console.log(...mp.entries());

a.unshift('a', 'v', 'e')
console.log(a)
let c = a.concat(b)
console.log(c)

a.splice(2, 0, 'guru', 'aaf', 'afee', 'aefe')
console.log(a)


class A {
    constructor(name, age) {
        console.log(this)
        this.name = name;
        this.age = age;
    }
    wish() {
        console.log(`hello ${this.name}`)
    }
}

class B extends A {
    constructor() {
        super(a, b)
        console.log(this)
        // super()
    }
}

let a = new A('guru', 10)