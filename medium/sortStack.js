function sortStack(stack) {
  // Write your code here.
	let solution = []
	sorting(stack, solution)
  return solution;
}

function sorting(stack, answer){
	console.log(stack, answer)
	if(!stack.length) return answer;
	if(!answer.length) {
			let currentValue = stack.pop()
			answer.push(currentValue)
	} else {
		
		let currentValue = stack.pop()
		let topValue = answer.pop()
		console.log(currentValue, topValue,currentValue > topValue)

		if(currentValue > topValue){
			answer.push(topValue)
			answer.push(currentValue)
		} else {
			let tempHolding = []
			tempHolding.push(topValue)

			while(topValue > currentValue){
				topValue = answer.pop()
				if(topValue>=currentValue){
						tempHolding.push(topValue)
				} else if(topValue){
						answer.push(topValue)
				}
			}

			answer.push(currentValue)

			while(tempHolding.length){
				answer.push(tempHolding.pop())
			}
		}
	}

	
	
	
// 	let currentValue = stack.pop()
// 	let topValue = answer.pop()
// 	// console.log(currentValue, topValue,currentValue > topValue)

// 	if(currentValue > topValue){
// 		answer.push(topValue)
// 		answer.push(currentValue)
// 	} else{
// 		let tempHolding = []
// 		tempHolding.push(topValue)
		
// 		while(topValue > currentValue){
// 			topValue = answer.pop()
// 			tempHolding.push(topValue)
// 		}
		
// 		answer.push(currentValue)
		
// 		while(tempHolding.length){
// 			answer.push(tempHolding.pop())
// 		}
// 	}
	
	sorting(stack, answer)
	
}

// Do not edit the line below.
exports.sortStack = sortStack;

