def getNthFib(n):
    # Write your code here.

	return fibo(n-1)
	
	
	
    
def fibo(n):
	if n == 0:
		return 0;
	if n == 1:
		return 1;
	else:
		return fibo(n-1) + fibo(n-2);
	