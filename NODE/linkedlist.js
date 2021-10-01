// let myLinkedList = {
//     head: {
//         value: 10,
//         next: {
//             value: 5,
//             next: {
//                 value: 6,
//                 next: null
//             }
//         }
//     }
// }
class Node {
    constructor(value) {
        this.value = value;
        this.next = null
    }
}
class LinkedList {
    constructor(value) {
        this.head = new Node(value);
        this.tail = this.head;
        this.length = 1;
    }
    append(value) {
        let newNode = {
            value: value,
            next: null
        }
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }
    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head
        this.head = newNode;
        this.length++;
        return this;
    }
    insert(index, value) {
        if (index >= this.length) {
            return this.append(value);
        }
        let newNode = new Node(value);
        let leader = this.traverseIndex(index - 1);
        let holdingPointer = leader.next;
        leader.next = newNode;
        newNode.next = holdingPointer;
        this.length++;
        return this.prinList();
    }
    remove(index) {
        let leader = this.traverseIndex(index - 1);
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;
        this.length--;
        return this.prinList();
    }
    traverseIndex(index) {
        let counter = 0;
        let currentNode = this.head;
        while (counter < index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }
    prinList() {
        const array = [];
        let currentNode = this.head;
        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
    reverse() {
        if (this.length === 1) {
            return this.head
        }
        let first = this.head;
        this.tail = this.head;
        let second = first.next;
        while (second) {
            const temp = second.next;
            second.next = first;
            first = second;
            second = temp;
        }
        this.head.next = null;
        this.head = first;
        return this.prinList();
    }
    reverse2() {
        let first = this.head;
        this.tail = this.head;
        let current = this.head.next;
        // let holder = null;
        while (current) {
            let holder = current.next;
            current.next = first;
            first = current;
            current = holder;
        }
        this.head.next = null;
        this.head = first;
    }
}
const myLinkedList = new LinkedList(10);
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(20)
myLinkedList.insert(2, 40)

// console.log(myLinkedList)
console.log(myLinkedList.prinList())
myLinkedList.traverseIndex(2)
console.log(myLinkedList.prinList())

myLinkedList.reverse2()
console.log(myLinkedList.prinList())
// console.log(myLinkedList)