function twoNumberSum(array, targetSum) {
    // Write your code here.
      let temp={};
      for(let i of array){
          let rem = targetSum - i;
          if(rem in temp) {
              return[rem,i]
          }else{
              temp[i] = i
          }
      }
      return []
  }
  
  // Do not edit the line below.
  exports.twoNumberSum = twoNumberSum;
  