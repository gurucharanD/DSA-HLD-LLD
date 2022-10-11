function threeNumberSum(array, targetSum) {
	
	let triplets=[]
	
	array.sort((a,b)=>a-b)
	
	for(let i =0;i<array.length;i++){
		
		let left = i+1;
		let right = array.length-1;
		
		while(left < right){
			
			let sum = array[i] + array[left] + array[right]
			
			if(targetSum == sum){
				triplets.push([array[i],array[left],array[right]])
				left ++
				right--
			} else if(sum < targetSum){
				left ++
			} else if(sum > targetSum){
				right --
			}
		}	
	}
	
	return triplets
	
  // Write your code here.
}

// Do not edit the line below.
exports.threeNumberSum = threeNumberSum;


// below solution has duplicates

// function threeNumberSum(array, targetSum) {
	
// 	let triplets=[];
// 	array.sort((a,b)=>a-b)
	
// 	for(let i = 0 ; i<array.length ; i++){
		
// 		let newTarget = targetSum - array[i];
// 		let temps = {}
// 		let tripletsSet = []
		
// 		for(let j = 0; j < array.length; j++){ 
			
// 			let diff = newTarget - array[j]
			
// 			if( diff in temps) {
				
// 				tripletsSet.push(array[i],diff,array[j])
// 				triplets.push(tripletsSet)
// 				break;
				
// 			} else {
				
// 				temps[ array[j] ] = array[j]
				
// 			}
			
// 		}
		
// 	}
	
// 	return triplets
// }

// // Do not edit the line below.
// exports.threeNumberSum = threeNumberSum;
