//O(nlogn)

function minHeightBst(array) {
    // Write your code here.
    return minDepthBST(array, null, 0, array.length - 1)
}

function minDepthBST(array, bst, left, right) {
    if (left > right) {
        return
    }

    let midIndex = Math.floor((left + right) / 2)
    let elemToInsert = array[midIndex]

    if (bst == null) {
        bst = new BST(elemToInsert)
    } else {
        bst.insert(elemToInsert)
    }

    minDepthBST(array, bst, left, midIndex - 1)
    minDepthBST(array, bst, midIndex + 1, right)
    return bst
}

class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        if (value < this.value) {
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                this.left.insert(value);
            }
        } else {
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                this.right.insert(value);
            }
        }
    }
}

// Do not edit the line below.
exports.minHeightBst = minHeightBst;


//////////////////////////////////////////

//O(nlogn)

function minHeightBst(array) {
    // Write your code here.
    return minCost(array, null, 0, array.length - 1)
}

function minCost(array, bst, left, right) {
    if (left > right) {
        return
    }

    let midIndex = Math.floor((left + right) / 2)
    let elemToInsert = array[midIndex]

    let newNode = new BST(elemToInsert)


    if (bst == null) {
        bst = newNode
    } else {
        if (elemToInsert < bst.value) {
            bst.left = newNode
            bst = bst.left
        } else {
            bst.right = newNode
            bst = bst.right
        }
    }



    minCost(array, bst, left, midIndex - 1)
    minCost(array, bst, midIndex + 1, right)
    return bst
}

class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    insert(value) {
        if (value < this.value) {
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                this.left.insert(value);
            }
        } else {
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                this.right.insert(value);
            }
        }
    }
}

// Do not edit the line below.
exports.minHeightBst = minHeightBst;

//////////////////////////////////////////

function minHeightBst(array) {
    // Write your code here.
      return minCost(array,0,array.length-1)
  }
  
  function minCost(array,left,right){
      if(left > right){
          return null
      }
      
      let midIndex = Math.floor((left+right)/2)
      let elemToInsert = array[midIndex]
      
      let newNode = new BST(elemToInsert)
  
      newNode.left = minCost( array, left, midIndex-1 ) 
      newNode.right = minCost( array, midIndex+1, right )
      return newNode
      
  }
  
  class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  
    insert(value) {
      if (value < this.value) {
        if (this.left === null) {
          this.left = new BST(value);
        } else {
          this.left.insert(value);
        }
      } else {
        if (this.right === null) {
          this.right = new BST(value);
        } else {
          this.right.insert(value);
        }
      }
    }
  }
  
  // Do not edit the line below.
  exports.minHeightBst = minHeightBst;
  