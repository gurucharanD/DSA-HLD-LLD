function moveElementToEnd(array, toMove) {
	
	let i =0;
	let j = array.length - 1;
	
	while(i<j){
		
		if(array[j] == toMove){
			j--
		} else if(array[i]==toMove){
			[array[i],array[j]]=[array[j],array[i]]
			i++
			j--
		} else{
			i++
		}
		
	}
	
	return array
  // Write your code here.
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;
