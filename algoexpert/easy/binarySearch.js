function binarySearch(array, target) {
	
	let left = 0;
	let right = array.length - 1;
	
		while(left <= right ){
				let mid = Math.floor((left + right) / 2);
				if( array[mid] == target ){
					return mid
				}

				if(target > array[mid]){
					left = mid+1
				} else {
					right = mid-1
				}
		}
		return -1
		
	}
	

  // Write your code here.


// Do not edit the line below.
exports.binarySearch = binarySearch;
