/**
  returns array
  since the array is sorted and can contain negative values, 
  the largest element in the sorted squares array comes from either the first element of last element
  comapre the first and last elements of array and find the biggest element among them
  and fill the array in reverse order from end to start
 */
function sortedSquaredArray(array) {
    // Write your code here.

    let smallIndex = 0;
    let largeIndex = array.length - 1;
    let currentInsertionIndex = array.length - 1;
    let squaredArray = [];

    while (smallIndex <= largeIndex) {
        let element1, element2, elementToConsider;

        element1 = Math.abs(array[smallIndex])
        element2 = Math.abs(array[largeIndex])

        if (element1 < element2) {
            elementToConsider = element2;
            largeIndex--;
        } else {
            elementToConsider = element1;
            smallIndex++;
        }
        squaredArray[currentInsertionIndex] = elementToConsider * elementToConsider
        currentInsertionIndex--
    }


    return squaredArray;
}

// Do not edit the line below.
exports.sortedSquaredArray = sortedSquaredArray;


//  BRUTEFORCE

// function sortedSquaredArray(array) {
//     // Write your code here.
//       let temp=[];
//       for(let i =0;i<array.length;i++){
//           temp.push(array[i]*array[i])
//       }
//     return temp.sort((a,b)=>a-b);
//   }

//   // Do not edit the line below.
//   exports.sortedSquaredArray = sortedSquaredArray;


// def sortedSquaredArray(array):
//     # Write your code here.
// 	print(array)
// 	startIndex = 0
// 	endIndex = len(array)-1
// 	indexToInsert = len(array)-1
// 	sortedArray=[0 for _ in array]
	
// 	while startIndex <= endIndex:
// 		elem1 = abs(array[startIndex])
// 		elem2 = abs(array[endIndex])
// 		elemToInsert=''
		
// 		if elem1 >= elem2:
// 			elemToInsert = elem1
// 			startIndex+=1
// 		else:
// 			elemToInsert = elem2
// 			endIndex-=1
			
// 		sortedArray[indexToInsert]=elemToInsert*elemToInsert
// 		print(elemToInsert,indexToInsert,sortedArray)

// 		indexToInsert-=1

		
// 	print(sortedArray)
			
	
//     return sortedArray

