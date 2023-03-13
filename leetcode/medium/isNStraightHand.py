from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        
        counter = Counter(hand)
        
        ans = 0
        for num in hand:
            if counter[num]:
                count = 0
                temp = []
                for i in range(num,num+groupSize):
                    if i in counter and counter[i]:
                        temp.append(i)
                        counter[i]-=1
                        count+=1

                if count == groupSize:
                    print(temp)
                    ans +=1
        
        print(ans)
        return ans*groupSize == len(hand)