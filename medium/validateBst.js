// This is an input class. Do not edit.
class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function validator(node, min, max) {
    if (node == null) return true

    if (node.value < min || node.value >= max) return false

    return validator(node.left, min, node.value) && validator(node.right, node.value, max)
}

function validateBst(tree) {
    return validator(tree, -Infinity, Infinity)
}

// Do not edit the line below.
exports.BST = BST;
exports.validateBst = validateBst;
