function merge(array1,array2){
  let length1 = array1.length;
  let length2 = array2.length;
  
  if(length1 == 0){
    return array2;
  }
  
  if(length2 == 0){
    return array1;
  }
  
  let pointer1 = 0;
  let pointer2 = 0;
  let sortedArray = [];
  
  while( pointer1<length1 && pointer2<length2 ){
    
    if(array1[pointer1]<=array2[pointer2]){
      sortedArray.push(array1[pointer1]);
      pointer1++;
    }else{
      sortedArray.push(array2[pointer2]);
      pointer2++;
    }
    
  }
  
  console.log(pointer1,pointer2)
  
  if(pointer1 == length1){
    for(let i = pointer2;i<length2; i++){
      sortedArray.push(array2[i]);
    }
    
  }else if(pointer2 == length2){
     for(let i = pointer1; i<length1; i++){
       sortedArray.push(array1[i]);
    }
  }
  
  return sortedArray;
  
}


// console.log(merge(
// [],
// []  
// ));

console.log(merge(
[1,3,5,8,45,67,89],
[2,4,6,11,23]  
));