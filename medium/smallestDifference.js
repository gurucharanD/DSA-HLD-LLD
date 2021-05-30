function smallestDifference(arrayOne, arrayTwo) {
	
	arrayOne.sort((a,b)=>a-b)
	arrayTwo.sort((a,b)=>a-b)

	let leftIndex = 0
	let rightIndex = 0
	let smallest = Infinity
	let comb=[]
	
	while(leftIndex<arrayOne.length && rightIndex<arrayTwo.length){
		if( arrayOne[leftIndex] == arrayTwo[rightIndex] ){
			return [arrayOne[leftIndex],arrayTwo[rightIndex]]
		}
		
		let diff = Math.abs(arrayOne[leftIndex]-arrayTwo[rightIndex])
		if(diff < smallest){
			smallest = diff
			comb = [arrayOne[leftIndex],arrayTwo[rightIndex]]
			// leftIndex++
			// rightIndex++
		}
		
		if(arrayOne[leftIndex]<arrayTwo[rightIndex]){
			leftIndex++
		}else{
			rightIndex++
		}
	}
	
	return comb
  // Write your code here.
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
