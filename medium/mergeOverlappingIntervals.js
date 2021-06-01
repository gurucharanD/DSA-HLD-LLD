function mergeOverlappingIntervals(array) {
	
	array.sort((a,b)=>a[0]-b[0])
	console.log(array)
	let i = 0
	
	while(i < array.length-1){
		let currentSlot = array[i]
		let nextSlot = array[i+1]
		
		if(currentSlot[1] >= nextSlot[0] && currentSlot[1] >= nextSlot[1]){
			 array.splice(i+1, 1);
		} else if(currentSlot[1] >= nextSlot[0]){
			 currentSlot[1] = nextSlot[1]
			 array.splice(i+1, 1);
		} else {
			i++
		}
	}
  // Write your code here.
  return array;
}

// Do not edit the line below.
exports.mergeOverlappingIntervals = mergeOverlappingIntervals;
