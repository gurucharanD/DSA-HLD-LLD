class Solution:
    def myAtoi(self, ele: str) -> int:
        
        
        ele = ele.strip()        
        if len(ele)==0:
            return 0
        
        sign =-1 if ele[0]=='-' else 1
        
        i = 0
        if ele[0] == '+' or ele[0] == '-':
            i = 1
            
        res = ''
        
        while i<len(ele) and ele[i].isdigit():
            res+=ele[i]
            i+=1
        
        res = int(res) if res else 0
        return max(-2**31,min(sign*res,2**31-1))