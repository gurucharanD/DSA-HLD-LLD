class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
      
        charArray = [ _ for _ in s]
        sol = []
        
        def helper(arr,index):
            if index == len(arr):
                sol.append("".join(arr))
                return
            
            helper(arr,index+1)
            
            if not charArray[index].isdigit():
                if arr[index].islower():
                    arr[index] = arr[index].upper()
                    helper(arr,index+1)
                    arr[index] = arr[index].lower()
                else:
                    arr[index] = arr[index].lower()
                    helper(arr,index+1)
                    arr[index] = arr[index].upper()

        helper(charArray,0)
        return sol