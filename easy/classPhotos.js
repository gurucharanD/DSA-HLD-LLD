function classPhotos(r, b) {
    // Write your code here.
      let result = true;
      
      let firstRow,secondRow;
      
      if( r[0] >= b[0] ){
          secondRow = r
          firstRow = b
      } else {
          secondRow = b
          firstRow = r
      }
      
      firstRow.sort((a,b)=>a-b)
      secondRow.sort((a,b)=>a-b)
  
      for( let i = 0; i < firstRow.length; i++  ){
          if( firstRow[i] >= secondRow[i] ) {
              result = false;
              break;
          }
      }
      
  
      
      
      
      
    return result;
  }
  
  // Do not edit the line below.
  exports.classPhotos = classPhotos;
  