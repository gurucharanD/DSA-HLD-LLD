class Node {
    constructor(value) {
        this.value = value;
        this.next = null
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.botom = null;
        this.length = 0;
    }
    push(value) {
        const newNode = new Node(value);
        if (this.length = 0) {
            this.top = newNode;
            this.botom = newNode;
        } else {
            const holdingPointer = this.top;
            this.top = newNode;
            this.top.next = holdingPointer;
        }
        this.length++;
        return this;
    }
    peek() {
        return this.top;
    }
    pop() {
        if (!this.top) {
            return null;
        }
        if (this.top === this.botom) {
            this.botom = null;
        }
        // const holdingPointer = this.top;
        this.top = this.top.next;
        this.length--;
        return this;
    }
}

const stack = new Stack();
stack.push(5)
stack.push(6)
stack.push(7)
console.log(stack.peek());
stack.pop()
stack.pop()
stack.pop()
console.log(stack.peek());