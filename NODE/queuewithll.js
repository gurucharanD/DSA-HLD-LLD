class Node {
    constructor(value) {
        this.value = value;
        this.next = null
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }
    enqueue(value) {
        const newNode = new Node(value);
        if (this.length === 0) {
            this.first = newNode;
            this.last = newNode;
        } else {
            //  let holdingPointer=this.last;
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;

    }
    dequeue() {
        if (this.length === 0) {
            return null;
        }
        if (this.first === this.last) {
            // let holdingPointer = this.first;
            this.last = null;
        }
        // let holdingPointer = this.first;
        this.first = this.first.next;
        this.length--;
        return this.first;
    }
    peek() {
        return this.first;
    }

}

const queue = new Queue();
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
console.log(queue.peek());
queue.dequeue()
console.log(queue.peek());