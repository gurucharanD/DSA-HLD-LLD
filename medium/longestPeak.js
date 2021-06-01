function longestPeak(array) {
    // Write your code here.
      
      let peaks=[]
      
      for(let i = 1; i<array.length-1; i++){
          if(array[i]>array[i-1] && array[i]>array[i+1]){
              peaks.push(i)
          }
      }
      
      let maxPeak = 0
      
      for(let j = 0; j < peaks.length; j++){
          
          console.log(peaks[j])
          let left = peaks[j]-1
          let right = peaks[j]+1
          console.log(right,left)
  
          while(array[left-1] < array[left] && left>0){
              left--
          }
          
          while(array[right+1] < array[right] && right < array.length){
              right++
          }
          
          console.log(right,left)
          let currentPeak = right - left
          
          if(currentPeak > maxPeak ){
              maxPeak = currentPeak +1
          } 
      }
      
      return maxPeak
      
  }
  
  // Do not edit the line below.
  exports.longestPeak = longestPeak;
  