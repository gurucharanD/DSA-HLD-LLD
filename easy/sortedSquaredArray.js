/**
  returns array
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
