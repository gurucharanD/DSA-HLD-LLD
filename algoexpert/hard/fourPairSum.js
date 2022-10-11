function fourNumberSum(array, targetSum) {
	const allPairSums = {};
	const quadraplets = [];
	
	for(let i =1;i<array.length-1;i++){
		for(let j = i+1;j<array.length;j++){
			const currentSum = array[i]+array[j]
			const difference = targetSum - currentSum;
			
			if(difference in allPairSums){
				for(const pair of allPairSums[difference]){
					quadraplets.push(pair.concat([array[i],array[j]]))
				}
			}
		}
		
		for(let k = 0;k<i;k++){
			const currentSum = array[i]+array[k]
			if(!(currentSum in allPairSums)){
				allPairSums[currentSum] = [[array[k],array[i]]]
			}else{
				allPairSums[currentSum].push([array[k],array[i]])
			}
		}
	}
	return quadraplets;
}

// Do not edit the line below.
exports.fourNumberSum = fourNumberSum;


/*
using the idea that,
if a+b+c+d = x
we can assume that or we can break it down into sum of pairs
p = a+b
q = c+d

we can strongly prove that p + q = x

to achieve this we need to loop over the array and find the pairs 
of numbers {p,q}

we can maintain p and q in a hash map and save the pairs of [a,b],[c,d]
in a hash map example:
{
    p:[{a,b},{a,c}]
    q:[{c,d}]
}

we need to make sure that we need to avoid making duplicates. for this

we loop over the array of elemetns in two directions

in first loop, we go in the direction of i to n and 
see if exists a Q in the hashmap. 
if exists, we save the pair in final solution
else ignore the sum

in second loop, we go from 0 to n and 
save the P and Q to the hashmap

we need to do this to avoid duplicates
*/