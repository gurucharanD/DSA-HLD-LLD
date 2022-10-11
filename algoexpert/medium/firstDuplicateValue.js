/**
 * 
 * @param {*} array 
 * @returns 
 * optimal O(n) and O(1)
 */

function firstDuplicateValue(array) {
    // Write your code here.
      
      for(let i of array){
          let index = Math.abs(i)-1
          
          if( array[index] < 0 ) return Math.abs(i)
          else array[index] = -1 * array[index]
      }
      
    return -1;
  }
  
  // Do not edit the line below.
  exports.firstDuplicateValue = firstDuplicateValue;


  /**
 * 
 * @param {*} array 
 * @returns 
 * optimal O(n) and O(n)
 */

  function firstDuplicateValue(array) {
    // Write your code here.
      let seen = {}
      let index = -1
      
      for(let i of array){
          
          if(i in seen){
              
              return i
              // let tempIndex = seen[array[i]]
              // if(index == -1){
              // 	index = tempIndex
              // } else {
              // 	index = tempIndex < index ? tempIndex: index
              // }
              
          } else{
              seen[i] = i
          }
      }
      
   return -1
  }
  
  // Do not edit the line below.
  exports.firstDuplicateValue = firstDuplicateValue;
  