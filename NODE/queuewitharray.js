class Queue {
    constructor() {
        this.queue = [];
        this.length = 0;
    }
    enqueue(value) {
        this.queue.push(value);
        this.length++;
    }
    dequeue() {
        if (this.length === 0) {
            return null;
        }
        let element = this.queue[this.length - 1];
        delete this.queue[this.length - 1];
        this.length--;
        return element;

    }
    peek() {
        return this.queue[0];
    }

}

const queue = new Queue();
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
console.log(queue);
queue.dequeue()
console.log(queue);