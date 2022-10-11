function knapsackProblem(items, capacity) {

	const knapSackValues = []
	
	for(let i = 0; i<items.length+1; i++){
		const row = new Array(capacity+1).fill(0)
		knapSackValues.push(row)
	}
	
	for(let i = 1;i<items.length+1;i++){
		let currentWeight = items[i-1][1];
		let currentValue = items[i-1][0];
		
		for(let c = 0; c<capacity+1;c++){
			if(currentWeight>c){
				knapSackValues[i][c] = knapSackValues[i-1][c]
			}else{
				knapSackValues[i][c] = Math.max(knapSackValues[i-1][c],knapSackValues[i-1][c-currentWeight]+currentValue)
			}
		}
	}
	


	return 	[knapSackValues[items.length][capacity],getKnapsackValues(knapSackValues,items)]
	
}

	function getKnapsackValues(knapSackValues,items){
		let sequnce = []
		let i = knapSackValues.length-1;
		let c = knapSackValues[0].length-1;
		
		while(i>0){
			if(knapSackValues[i][c]==knapSackValues[i-1][c]){
				i -= 1
			}else{
				sequnce.unshift(i-1)
				c-=items[i-1][1]
				i-=1
			}
			
			if(c==0)
				break
		
		}
			return sequnce

	}

// Do not edit the line below.
exports.knapsackProblem = knapsackProblem;
