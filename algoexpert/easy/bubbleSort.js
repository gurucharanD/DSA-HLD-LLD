function bubbleSort(a) {
	for(let i = 0; i < a.length ;i++){
		for(let j = i+1 ; j < a.length ; j++){
			if(a[i]>a[j]){
				let temp = a[i]
				a[i] = a[j]
				a[j] = temp
			}
		}
	}
	return a
  // Write your code here.
}

// Do not edit the line below.
exports.bubbleSort = bubbleSort;


function bubbleSort(a) {
	for(let i = 0; i < a.length - 1 ;i++){
		
		for(let j = 0 ; j < a.length - (i+1) ; j++){
			
			if(a[j]>a[j+1]){
				
				let temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
				
			}
			
		}
	}
	return a
  // Write your code here.
}

// Do not edit the line below.
exports.bubbleSort = bubbleSort;
