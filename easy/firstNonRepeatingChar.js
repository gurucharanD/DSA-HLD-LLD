function firstNonRepeatingCharacter(string) {
    // Write your code here.
      let count = {}
      for( let  i of string){
          if( i in count){
              count[i]++
          }else{
              count[i]=1
          }
      }
      
      for(let i=0; i < string.length;i++){
          if(count[string[i]]==1) return i
      }
    return -1;
  }
  
  // Do not edit the line below.
  exports.firstNonRepeatingCharacter = firstNonRepeatingCharacter;
  