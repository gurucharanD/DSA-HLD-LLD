function sunsetViews(buildings, direction) {
	
	let stack=[]
	
	let solution=[]
	
	if(direction == "EAST"){
		for(let i = 0; i<buildings.length; i++){
			stack.push({
				id:i,
				height:buildings[i]
			})
		}
	}else{
		for(let i = buildings.length-1;i>=0;i--){
			stack.push({
				id:i,
				height:buildings[i]
			})
		}
	}
			// console.log(stack)

	for(let i = stack.length-1;i>=0;i--){
		// console.log(i)
		if(!solution.length){
			solution.push(stack[i])
		} else {
			let top = solution[solution.length-1]
			// console.log(stack[i].height > top.height,stack[i].height , top.height)
			if(stack[i].height > top.height){
				solution.push(stack[i])
			}
			// stack.pop()
		}
	}
  // Write your code here.
	// console.log(solution)
		if(direction == "EAST"){
			solution = solution.reverse()
		}
				return solution.map(x=>x.id)

	
  return [];
}

// Do not edit the line below.
exports.sunsetViews = sunsetViews;
