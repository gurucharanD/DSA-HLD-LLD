// Tip: You can use the Array.isArray function to check whether an item
// is a list or an integer.
function productSum(array) {
    // Write your code here.
      return special(array,1)
  }
  
  function special(array,level){
          console.log(array,level)
  
      let sum = 0;
      for(let i of array){
          if(i.length){
              sum += level*special(i, level+1)
          } else {
              sum += i * level
          }
      }
      
      return sum;
  }
  
  // Do not edit the line below.
  exports.productSum = productSum;
  