class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_LETTERS = {
            "":[],
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }
        
        if digits == "":
            return []
        
        def helper(index,digits,currentComb,solution):
            if index == len(digits):
                solution.append("".join(currentComb))
            else:
                letters = DIGIT_LETTERS[digits[index]]
                for letter in letters:
                    currentComb[index] = letter
                    helper(index+1,digits,currentComb,solution)
                
        
        currentComb = [0]*len(digits)
        solution = []
        helper(0,digits,currentComb,solution)
        return solution