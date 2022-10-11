function runLengthEncoding(string) {
	let char = string[0]
	let count =1
	let str=''
	
	for(let i = 1; i < string.length; i++){
		
		if(count == 9 || char !== string[i]){
				str += count+char
				char = string[i]
				count = 0
		}
		count++
		
	}
	
	return str + count + char
  // Write your code here.
}

// Do not edit the line below.
exports.runLengthEncoding = runLengthEncoding;
