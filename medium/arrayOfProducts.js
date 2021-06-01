function arrayOfProducts(array) {
  // Write your code here.
	
	let leftProduct = []
	let rightProduct = []
	let product = []
	
	leftProduct[0]=1
	rightProduct[array.length-1]=1
	
	for(let i =1; i<array.length; i++){
		leftProduct[i] = leftProduct[i-1]*array[i-1]
	}
	
	for(let i = array.length-2; i>=0; i--){
		rightProduct[i] = rightProduct[i+1]*array[i+1]
	}
	
	for(let i =0; i<array.length; i++){
		product[i] = leftProduct[i]*rightProduct[i]
	}
	
	return product
	
}

// Do not edit the line below.
exports.arrayOfProducts = arrayOfProducts;
