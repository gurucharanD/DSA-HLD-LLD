function findClosestValueInBst(tree, target) {
	
	let nearest = tree?.value ?? null
	while(tree?.value){
		let distance = Math.abs( tree.value - target );
		
		if(distance < Math.abs( nearest - target )){
			nearest = tree.value;
		}
		
		if(target < tree.value){
			tree = tree.left
		}else{
			tree = tree.right
		}
	}
	return nearest
  // Write your code here.
}

// This is the class of the input tree. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.findClosestValueInBst = findClosestValueInBst;
