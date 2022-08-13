# insert each number as a 32 bit represenation and insert them into Trie from 32 bit to 1 bit
# start iterating over every number and find the maximum xor that could be formed with these numbers
# initially the answer is 0
# at every bit find if the opposite of this current bit is found in the trie
# if the opposite bit is found make the ith bit of the answer as one and move to the next bit
# else go to the bit found 


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, num: str) -> None:
        current = self.root
        for i in range(31,-1,-1):
            bit =  ( num >> i ) & 1
            if bit not in current:
                current[bit] = {}
            current = current[bit]
            
        current['*'] = True
        
    def search(self, num: int) -> bool:
        current = self.root
        sol = 0
        for i in range(31,-1,-1):
            bit = ( num >> i )&1
                        
            if (1-bit) in current:
                sol = sol | (1 << i)
                current = current[1-bit]
            else:
                current = current[bit]
            
        return sol


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()
        
        for num in nums:
            trie.insert(num)
        
        ans = 0
        for num in nums:
            ans = max(ans,trie.search(num))
            
        return ans
                
                
                
                
                