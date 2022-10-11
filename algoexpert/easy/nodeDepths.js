function nodeDepths(root) {
    // Write your code here.
      let depth = 0;
      let cuurentDepth = 0;
      return findDepth(root,depth,cuurentDepth)
      // return cuurentDepth
  }
  
  function findDepth(root,  cuurentDepth = 0){
  
      console.log(root?.value, cuurentDepth)
  
      if(root == null){
          return 0
      }
  
      return cuurentDepth + findDepth(root?.left, cuurentDepth + 1) + findDepth(root?.right, cuurentDepth + 1) 
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
  exports.nodeDepths = nodeDepths;
  