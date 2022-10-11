function getNthFib(n) {
	
	if(n == 1) return 0;
	if(n == 2) return 1;
	
	let a = 0;
	let b = 1;
	
	let i = 3;
	let c;
	

	
	while( i <= n){
		c = a+b;
		a = b;
		b = c;
		i++
	}
	
	return c
	
}

// Do not edit the line below.
exports.getNthFib = getNthFib;


function getNthFib(n) {
	
	return fibo(n)
  // Write your code here.
}

function fibo(n,memo={}){
	if(n in memo) return memo[n];
	if( n == 1) return 0;
	if(n <= 3) return 1;
	memo[n] = fibo( n-1 , memo ) + fibo( n-2 , memo )
	return memo[n]
}

// Do not edit the line below.
exports.getNthFib = getNthFib;
