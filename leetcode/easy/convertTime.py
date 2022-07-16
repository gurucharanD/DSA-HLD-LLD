class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        corrections = [1,5,15,60]
        count = 0
        correct = int(''.join(correct[0:2]))*60 + int(''.join(correct[3:]))                         
        current = int(''.join(current[0:2]))*60 + int(''.join(current[3:]))
                
        totalDiff = correct - current
                
        while totalDiff > 0:
            
            if totalDiff in corrections:
                count += 1
                totalDiff = 0
            else:
                for j in range(0,len(corrections)):
                    if corrections[j] < totalDiff:
                        divisor = corrections[j]
                    else:
                        break
                                
                count+=totalDiff//divisor
                totalDiff = totalDiff % divisor
                
        return count
        