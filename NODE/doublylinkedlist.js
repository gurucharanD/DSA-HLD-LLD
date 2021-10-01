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
        this.prev = null;
    }
}
class DoublyLinkedList {
    constructor(value) {
        this.head = new Node(value);
        this.tail = this.head;
        this.length = 1;
    }
    append(value) {
        let newNode = new Node(value);
        newNode.prev = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }
    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head
        newNode.prev = null;
        this.head = newNode;
        this.head.prev = newNode;
        this.length++;
        return this;
    }
    insert(index, value) {
        if (index >= this.length) {
            return this.append(value);
        }
        let newNode = new Node(value);
        let leader = this.traverseIndex(index - 1);
        let follower = leader.next;
        leader.next = newNode;
        newNode.next = follower;
        newNode.prev = leader;
        follower.prev = newNode;
        this.length++;
        return this.prinList();
    }
    remove(index) {
        let leader = this.traverseIndex(index - 1);
        const unwantedNode = leader.next;
        let follower = unwantedNode.next;
        follower.prev = leader;
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
}
const myLinkedList = new DoublyLinkedList(10);
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(20)
myLinkedList.insert(2, 40)
myLinkedList.remove(3)
console.log(myLinkedList.prinList())