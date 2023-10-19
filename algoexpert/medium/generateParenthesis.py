# 22. Generate Parentheses
# maintain the count of opening and closing paranthesis

# complexity of each function is O(1)
# and there are 2^n recursion calls in worst case
# so, the time complexity is O(2^n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        solution = []
        def helper(s,opening,closing,solution):
            if opening == 0 and closing == 0:
                solution.append(s)
                return
            
            if opening > 0 :
                s+='('
                helper(s,opening-1,closing,solution)
                # backtrack step remove the last added
                # parenthesis and go to next branch
                s = s[:-1]
            
            if closing > 0: 
                # this condition is inplce to prevent us
                # from starting a new combination with
                # a closing ), if we start with a open (
                # the count of closing is always greater
                # than the opening
                if opening < closing:
                    s+=')'
                    helper(s,opening,closing-1,solution)
                    s = s[:-1]
            
            
        helper('',n,n,solution)
            
        
        
        return solution
            
        