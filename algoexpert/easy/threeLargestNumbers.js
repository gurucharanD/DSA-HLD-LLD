function findThreeLargestNumbers(array) {
	
	let firstLargestElement = null
	let secondLargestElemnet = null
	let thirdLargestElement = null
	
	for(let i of array){
		
		if( firstLargestElement == null || i > firstLargestElement){
			thirdLargestElement = secondLargestElemnet
			secondLargestElemnet = firstLargestElement
			firstLargestElement =  i
		} else if ( secondLargestElemnet == null || i > secondLargestElemnet ){
				thirdLargestElement = secondLargestElemnet
				secondLargestElemnet = i
		} else if ( thirdLargestElement == null || i > thirdLargestElement){
				thirdLargestElement = i
		}
		
	}
	
  // Write your code here.
	return [thirdLargestElement,secondLargestElemnet,firstLargestElement]
}

// Do not edit the line below.
exports.findThreeLargestNumbers = findThreeLargestNumbers;
