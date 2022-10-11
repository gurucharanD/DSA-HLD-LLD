// This is an input class. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function findKthLargestValueInBst(tree, k) {
  // Write your code here.
	let inOrder = inOrderTraverse(tree, [])
  console.log(inOrder)
	if(inOrder.length){
		return inOrder[inOrder.length-k]
	}
	return -1;
}

function inOrderTraverse(tree, array) {
  // Write your code here.
	if(tree == null) return array
	inOrderTraverse(tree.left, array)
	array.push(tree.value)
	inOrderTraverse(tree.right, array)
	return array
}

// Do not edit the lines below.
exports.BST = BST;
exports.findKthLargestValueInBst = findKthLargestValueInBst;
