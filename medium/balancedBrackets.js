function balancedBrackets(string) {
    // Write your code here.
      let stack = []
      for(let i of string ){
          if( i=='(' || i=='[' ||i=='{' ){
              
              stack.push(i)
              
          } else if( i==')' || i==']' ||i=='}' ){
              
              let elem = stack.pop();
              
              switch(i){
                      
                  case ')':
                      if(elem!=='(')
                          return false;
                      break;
                      
                  case ']':
                      if(elem!=='[')
                          return false;
                      break;	
                      
                  case '}':
                      if(elem!=='{')
                          return false;
                      break;
              }
          }
      }
      
      if(stack.length){
          return false
      }
      return true
  }
  
  // Do not edit the line below.
  exports.balancedBrackets = balancedBrackets;
  