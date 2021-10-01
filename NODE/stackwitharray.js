class StackWithArray {
    constructor() {

        this.length = 0;
        this.stack = [];
    }
    push(value) {
        this.stack.push(value);
        this.length++;
        return this;
    }
    pop() {
        let item = this.stack[this.length - 1];
        delete this.stack[this.length - 1];
        this.length--;
        return item;
    }
    peek() {
        return this.stack[this.length - 1];
    }
}

const stack = new StackWithArray()
stack.push(1)
stack.push(2)
stack.push(3)

console.log(stack)
console.log(stack.pop())
console.log(stack)