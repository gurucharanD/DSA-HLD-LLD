function caesarCipherEncryptor(string, key) {
	
	let solution='';
	 key = key %26
	
	for(let i of string){
		let charCode = i.charCodeAt();
		let newChatCode = charCode + key;
		
		if( newChatCode > 122){
			newChatCode = 96 + (newChatCode % 122)
		}
		console.log(i,key,charCode,newChatCode)
		solution += String.fromCharCode(newChatCode)
	}
	
	return solution
	
	
  // Write your code here.
}

// Do not edit the line below.
exports.caesarCipherEncryptor = caesarCipherEncryptor;
