// This is the class of the input root.
// Do not edit it.
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function branchSums(root) {
    // Write your code here.
      let temp=[]
       calculateSum(root,0,temp)
      return temp
  }
  
  function calculateSum(node,sum = 0,temp=[]){
      
      sum+=node.value
      
      if(!node?.right && !node?.left){
          temp.push(sum)
          return
      }
      if(node?.left){
          calculateSum(node.left,sum,temp)
      }
      if(node?.right){
          calculateSum(node.right,sum,temp)
      }
      return temp
  }
  
  // Do not edit the lines below.
  exports.BinaryTree = BinaryTree;
  exports.branchSums = branchSums;

