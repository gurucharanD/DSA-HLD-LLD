function nonConstructibleChange(coins) {
  // Write your code here.
	let currentChange = 0;
	coins.sort((a,b)=>a-b)
	for(let coin of coins){
		if(coin > currentChange + 1){
			return currentChange + 1
		}
		currentChange = currentChange + coin;
	}
  return currentChange+1;
}

// Do not edit the line below.
exports.nonConstructibleChange = nonConstructibleChange;



