function leastPositiveSum(array1,array2){
  
  array1 = array1.sort();
  array2 = array2.sort();
  
  console.log(array1,array2);

  let pointer1=0;
  let pointer2=0;
  
  let lengthOfArray1 = array1.length;
  let lengthOfArray2 = array2.length;
  
  while(pointer1<lengthOfArray1 && pointer2<lengthOfArray2){
    if(array1[pointer1]<0 && array2[pointer2]<0){
      pointer1++;
      pointer2++;
    }else{
      let sum = array1[pointer1]+array2[pointer2];
      if(sum<0){
        if(array1[pointer]<0){
          pointer1++;
        }else{
          pointer2++;
        }
      }else{
        return sum;
      }
    }
  }
}


console.log(leastPositiveSum(
  [-1,-2,3],
  [-1,-2,3]
))


console.log(leastPositiveSum(
  [-1,-2,0],
  [-1,-2,0]
))