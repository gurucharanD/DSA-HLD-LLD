class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }
    insert(value) {
        const node = new Node(value);
        if (this.root === null) {
            this.root = node;
        } else {
            let currentNode = this.root;
            while (true) {
                if (value < currentNode.value) {
                    //go left
                    if (!currentNode.left) {
                        currentNode.left = node;
                        return this;
                    }
                    currentNode = currentNode.left;
                } else {
                    // go right
                    if (!currentNode.right) {
                        currentNode.right = node;
                        return this;
                    }
                    currentNode = currentNode.right;
                }
            }
        }

    }
    lookup(value) {
        if (!root) {
            return false;
        }
        let currentNode = this.root;
        while (currentNode) {
            if (value < currentNode.value) {
                currentNode = currentNode.left;
            } else if (value > currentNode.value) {
                currentNode = currentNode.right;
            } else if (value = currentNode.value) {
                return currentNode;
            }
        }
        return false;
    }
    remove(value) {
        if (!this.root) {
            return false;
        }
        let currentNode = this.root;
        let parentNode = null;
        while (currentNode) {
            if (value < currentNode.value) {
                parentNode = currentNode;
                currentNode = currentNode.left;
            } else if (value > currentNode.vaLue) {
                parentNode = currentNode;
                currentNode = currentNode.right;
            } else if (currentNode.value === value) {
                if (currentNode.right === null) {
                    if (parentNode === null) {
                        this.root = currentNode.left;
                    } else {
                        if (currentNode.value < parentNode.value) {
                            parentNode.left = currentNode.left;
                        } else if (currentNode.vaLue > parentNode.value) {
                            parentNode.right = currentNode.left;
                        }
                    }
                }
            } else if (currentNode.right.left === null) {

            } else {

            }
        }

    }
    breadthFirstSearch() {
        let currentNode = this.root;
        let list = [];
        let queue = [];
        queue.push(currentNode);
        while (queue.length > 0) {
            currentNode = queue.shift();
            list.push(currentNode.value);
            if (currentNode.left) {
                queue.push(currentNode.left);
            }
            if (currentNode.right) {
                queue.push(currentNode.right);
            }
        }
        return list;
    }
    breadthFirstSearchR(queue, list) {
        if (!queue.length) {
            return list;
        }
        let currentNode = queue.shift();
        list.push(currentNode.vaLue);
        if (currentNode.left) {
            queue.push(currentNode.left);
        }
        if (currentNode.right) {
            queue.push(currentNode.right);
        }
        return this.breadthFirstSearchR(queue, list);
    }
    depthFirstSearchInOrder() {
        return traverseInOrder(this.root, []);
    }
    depthFirstSearchPreOrder() {
        return traversePreOrder(this.root, []);
    }
    depthFirstSearchPostOrder() {
        return traversePostOrder(this.root, []);
    }
}

function traverseInOrder(node, list) {
    if (node.left) {
        traverseInOrder(node.left, list);
    }
    list.push(node.value);
    if (node.right) {
        traverseInOrder(node.right, list);
    }
    return list;
}
function traversePreOrder(node, list) {
    list.push(node.value);
    if (node.left) {
        traversePreOrder(node.left, list);
    }
    if (node.right) {
        traversePreOrder(node.right, list);
    }
    return list;
}
function traversePostOrder(node, list) {
    if (node.left) {
        traversePostOrder(node.left, list);
    }
    if (node.right) {
        traversePostOrder(node.right, list);
    }
    list.push(node.value);
    return list;
}
function traverse(node) {
    const tree = {
        value: node.value
    };
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.left === null ? null : traverse(node.right);
    return tree;
}

const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
// console.log(tree.breadthFirstSearchR([tree.root], []));
console.log(tree.depthFirstSearchInOrder())
console.log(tree.depthFirstSearchPreOrder())
console.log(tree.depthFirstSearchPostOrder())

// console.log(tree.breadthFirstSearch());
// console.log(traverse(tree.root));
// console.log(tree.lookup(9));
