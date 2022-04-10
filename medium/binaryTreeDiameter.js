// This is an input class. Do not edit.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class TreeInfo{
	constructor(diameter,height){
		this.diameter = diameter
		this.height = height
	}
}

function getTreeInfo(tree){
	if(tree==null){
		return new TreeInfo(0,0)
	}
	
	const leftTreeInfo = getTreeInfo(tree.left)
	const rightTreeInfo = getTreeInfo(tree.right)
	
	const longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	const maxDiameterSoFar = Math.max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	
	const currentDiameter = Math.max(longestPathThroughRoot,maxDiameterSoFar)
	
	const currentHeight = 1+Math.max(leftTreeInfo.height,rightTreeInfo.height)
	
	return new TreeInfo(currentDiameter,currentHeight)
	
}

function binaryTreeDiameter(tree) {
  // Write your code here.
  return getTreeInfo(tree).diameter;
}

// Do not edit the line below.
exports.binaryTreeDiameter = binaryTreeDiameter;
exports.BinaryTree = BinaryTree;
