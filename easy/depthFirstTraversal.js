// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
    constructor(name) {
      this.name = name;
      this.children = [];
          this.traversed = [];
    }
  
    addChild(name) {
      this.children.push(new Node(name));
      return this;
    }
      
      traversal(node,children){
          console.log(node)
          this.traversed.push(node);
  
          if(!children.length)
              return
          
  
          for(let i of children){
              this.traversal(i.name,i.children)
          }
      }
  
    depthFirstSearch(array) {
      // Write your code here.
          // console.log(this)
          this.traversal(this.name, this.children)
          return this.traversed
    }
      
  }
  
  // Do not edit the line below.
  exports.Node = Node;
  