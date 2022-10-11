/**
 * 
 * @param {*} array 
 * @param {*} sequence 
 * @returns 
 * 
 * 
 * use two pointers technique, place one pointer at the begining of array and other at the beginging of second array.
 * if values of both arrays and sequence are equal increment both the pointers, else increment only array pointer
 * make sure there are no out of index exceptions 
 */
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
  

//   def isValidSubsequence(array, sequence):
// 	print(array,sequence)
// 	pointer1 = 0
// 	pointer2 = 0
	
// # 	if len(array) == 0 or len(sequence) == 0:
// # 		return []
	
// 	for i in range(len(array)):
// 		if pointer2 == len(sequence):
// 			return True
// 		if array[pointer1] == sequence[pointer2]:
// 			pointer2 = pointer2+1
			
// 		pointer1 = pointer1+1
			
			
// 	if pointer2 == len(sequence):
// 		return True
// 	else:
// 		return False

	

			
	
//     pass
