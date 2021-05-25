function isValidSubsequence(array, sequence) {
    // Write your code here.
      let j=0;
      
      for(let i = 0; i<array.length && j<sequence.length; i++){
          if(array[i] == sequence[j]){
              j++
          }
      }
      
      if(j == sequence.length){
          return true;
      }
      return false
      
  }
  
  // Do not edit the line below.
  exports.isValidSubsequence = isValidSubsequence;
  