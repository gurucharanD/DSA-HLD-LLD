// This is an input class. Do not edit.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
    this.parent = null;
  }
}

function findSuccessor(tree, node) {
  // Write your code here.
  let arr = []
  let ans = null;
  inOrder(tree, arr)
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].value == node.value) {
      ans = arr[i + 1]
      break
    }
    // console.log(arr[i],node.value)
  }
  console.log(ans)
  return ans;
}

function inOrder(tree, arr) {
  if (!tree?.value)
    return

  inOrder(tree.left, arr)
  arr.push(tree)
  inOrder(tree.right, arr)
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.findSuccessor = findSuccessor;

// above solution takes O(n) and can be further optimised

