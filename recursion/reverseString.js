function reverseString(input){
  if(input == ''){
    return ''
  }
  
  return reverseString(input.substring(1))+input[0]
}

console.log(reverseString('input'))