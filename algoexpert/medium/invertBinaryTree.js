function invertBinaryTree(tree) {
	let queue = [tree]
	while(queue.length){
		let curr = queue.shift()
		if(curr==null) continue 
		swap(curr)
		queue.push(curr.left)
		queue.push(curr.right)
	}
	
  // Write your code here.
}

function swap(node){
	let left = node.left
	node.left = node.right
	node.right = left
}

// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.invertBinaryTree = invertBinaryTree;
