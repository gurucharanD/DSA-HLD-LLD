# Approach: Sieve of Eratosthenes
# 204. Count Primes

# approach: assume all the numbers from one to n are prime numbers
# except number 0 and number 1
# all the prime numbers from 1 to n only fall below the sqrt(n)
# start looping i from 2 to sqrt(n) and mark all the multiples of i
# as not primes i.e isPrimes[i] = False

# at the end return all the numbers which have isPrimes[i] as True

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrime = [True for _ in range(n)]
        
        isPrime[0] = False
        isPrime[1] = False
        
        for i in range(2,int(sqrt(n))+1):
            
            if isPrime[i]:
                for j in range(i*i,n,i):
                    isPrime[j] = False
        
        # print(isPrime)
        count = 0
        for p in isPrime:
            if p:
                count+=1
        
        return count