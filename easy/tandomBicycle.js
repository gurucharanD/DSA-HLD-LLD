function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
    // Write your code here.
  let result = 0
  
  blueShirtSpeeds.sort((a,b)=>b-a)		
  
  if(fastest){
      redShirtSpeeds.sort((a,b)=>a-b)
  }else{
      redShirtSpeeds.sort((a,b)=>b-a)
  }
      
  for( let i = 0; i< redShirtSpeeds.length;i++ ){
  
      let max = Math.max(redShirtSpeeds[i],blueShirtSpeeds[i])
  
       result += max;
  }
      
    return result;
  }
  
  // Do not edit the line below.
  exports.tandemBicycle = tandemBicycle;
  