// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  // Write your code here.
	remove(linkedList,linkedList.next)
	return linkedList
	 
}

function remove(currentNode,nextNode){
	
	if(currentNode?.next == null){
		return
	}
	
	if(currentNode?.value == nextNode?.value){
		currentNode.next = nextNode?.next
		remove(currentNode,nextNode?.next)
		
	} else{
		
		remove(currentNode.next,nextNode?.next)
		
	}
	
}
// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.removeDuplicatesFromLinkedList = removeDuplicatesFromLinkedList;


// iterative

// This is an input class. Do not edit.
class LinkedList {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  function removeDuplicatesFromLinkedList(linkedList) {
      
      let Node = linkedList;
      
      while(Node?.next!=null){
          
          let nextNode = Node.next;
          
          if(Node.value == nextNode.value){
              Node.next = nextNode.next
          } else {
              Node = nextNode
          }
          
          
      }
    // Write your code here.
    return linkedList;
  }
  
  // Do not edit the lines below.
  exports.LinkedList = LinkedList;
  exports.removeDuplicatesFromLinkedList = removeDuplicatesFromLinkedList;
  