/**
optimal with only one loop
O(n) , O(1)
*/

function isMonotonic(array) {
    // Write your code here.
      if(array.length <=2 ) return true
    let order = ''
  
      for(let i = 0; i<array.length-1; i++ ){
          
          let prevOrder = order
          let diff = array[i] - array[i+1]
          if(diff == 0) continue
          
          if( diff < 0 ){
              order = 'desc'
          } else {
              order = 'asc'
          } 
          
          if(prevOrder !== '' && prevOrder !== order){
              return false
          }
                                  
      }
      return true
  }
  
  // Do not edit the line below.
  exports.isMonotonic = isMonotonic;
  

  /**
   * Brutforrce near optimal, has 2 loops
   * still O(n),O(1)
   */

   function isMonotonicBruteForce(array) {
	
	if(array.length <=2 ) return true
	
	let order=''
	
	for(let i =0;i<array.length;i++){
		if(array[i]==array[i+1])continue
		if(array[i] < array[i+1]){
			order = 'asc'
			break;
		}	else {
			order = 'desc'
			break;
		}
		
	}
	
		
	if(order == 'asc'){
		let i = 0;
		while(i < array.length-1){
			if(array[i] <= array[i+1]){
				i++
			}else{
				return false
			}
		}
	} else {
		let i = 0;
			while(i < array.length-1){
				if(array[i] >= array[i+1]){
					i++
				}else{
					return false
				}
			}
	}
	return true
  // Write your code here.
}

// Do not edit the line below.
exports.isMonotonicBruteForce = isMonotonicBruteForce;
