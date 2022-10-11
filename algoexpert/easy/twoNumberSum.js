/**
 * 
 * @param {*} array 
 * @param {*} targetSum 
 * @returns 
 * 
 * Hint: use a hashmap to save visited values
 * and eveytime check if a particula value exists inside hashmap
 * if the value exists return the [remainginsum, i ] 
 * else return [] at the end of loop
 * 
 */

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
  

//   def twoNumberSum(array, targetSum):
//     # Write your code here.
// 	temp = {}
// 	for i in array:
// 		rem = targetSum - i
// 		if ( rem in temp):
// 			return [rem,i]
// 		else:
// 			temp[i]=i
// 	return []
		
//     pass
