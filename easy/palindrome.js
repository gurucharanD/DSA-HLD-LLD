function isPalindrome(string) {
	let start = 0
	let end = string.length-1
	
	while(start <= end){
		console.log(string[start],string[end])
		if(string[start]==string[end]){
			start ++
			end --
		}else{
			return false
		}
	}
	return true
  // Write your code here.
}

// Do not edit the line below.
exports.isPalindrome = isPalindrome;
