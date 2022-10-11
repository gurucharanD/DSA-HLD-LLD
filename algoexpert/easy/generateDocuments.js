function generateDocument(characters, document) {
    // Write your code here.
      if(document=='') return true
      if(characters=='') return false
  
      
      let charsCount={}
      let docsCount={}
      
      for(let i of characters){
          if(i in charsCount){
              charsCount[i]+=1
          }else{
              charsCount[i]=1
          }
      }
      
      for(let j of document){
          if(j in docsCount){
              docsCount[j]+=1
          }else{
              docsCount[j]=1
          }
      }
      
      
      for( let k in docsCount ){
  
          if( !charsCount[k] || charsCount[k] < docsCount[k] ){
              return false;
          }
      }
      
    return true;
  }
  
  // Do not edit the line below.
  exports.generateDocument = generateDocument;
  