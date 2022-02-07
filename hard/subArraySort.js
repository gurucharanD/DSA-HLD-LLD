/**
 * 
    BRUTEFORCE : O(nlogn) due to sort and extra space O(n) for saving the sorted array and original array
    initialise start and end index to -1
    start looping over the original array and sorted array and compare elements index by index 
    if both the elements are same -> do nothing
    else -> if startIndex = -1 assign the index of mismatch to startIndex
            if startIndex != -1 keep updating the endIndex with index of mismatch

    after end of loop retunn [startIndex, endIndex]


 */
function subarraySort(array) {

	let originalArray = [...array]
	let sortedArray = array.sort((a,b)=>a-b)
	
	let startIndex = -1;
	let endIndex = -1;
	
    for (let i = 0; i < originalArray.length; i++){
        
		if(originalArray[i]!= sortedArray[i]){
			if(startIndex == -1){
				startIndex = i
			}
		
			if(startIndex != -1){
				endIndex = i
			}
		}

	}
	
	return [startIndex,endIndex]
}

// Do not edit the line below.
exports.subarraySort = subarraySort;



/** ---------------------------------------------------------------------- */


function subarraySort(array) {
	let minOutOfOrder = Infinity;
	let maxOutOfOrder = -Infinity;
	
	
	for(let i=0;i<array.length;i++){
		if(isOutOfOrder(array[i],i,array)){
			minOutOfOrder = Math.min(minOutOfOrder,array[i])
			maxOutOfOrder = Math.max(maxOutOfOrder,array[i])
		}
	}
	
	if(minOutOfOrder == Infinity) return [-1,-1];
	let subbarrayLeftIndex = 0;
	let subarrayRightIndex = array.length-1;
	
	while(array[subbarrayLeftIndex] <= minOutOfOrder){
		subbarrayLeftIndex++
	}
	while(array[subarrayRightIndex] >= maxOutOfOrder){
		subarrayRightIndex--
	}
	
	return [subbarrayLeftIndex,subarrayRightIndex];
}

function isOutOfOrder(num,i,array){
	if(i==0){
		return num > array[i+1]
	}
	
	if(i == array.length-1){
		return num < array[i-1]
	}
		
	return num < array[i-1] || num > array[i+1]
}

// Do not edit the line below.
exports.subarraySort = subarraySort;


/**
 * loop over the input array and find the part of the input array that is not sorted
 * while looping find the min and max elements of the unsorted part of the input array
 * 
 * after the loop ends find the position of the min and max elements of the unsorted array
 * initialise leftIndex of subarray to 0 and rightIndex of subarray to length of array-q
 * 
 * using the idea that array[i]<= min element of unsorted array increment left Index
 * array[i]>= max element of unsorted array decrement right index
 * 
 * the final values of left and right indxes will be indexes at which the minimum unsorted array begins
 * 
 */