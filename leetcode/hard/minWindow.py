# maintain two counts required and available
# required shows the number of unique characters needed
# available shows the count of unique characaters found in the current window
# if required == available in a window, then we have found a possible answer

# the value of available is incremented when we add a character into our window which is 
# avaialable in t and the count of it in the window and the counter is equal

# once the condition is meet, we need to compare it with the answer we already have
# to find the best answer 

# keep incrementing the window until, the condition available == required is not satisfied
# once the condition is satisfied shrink the window by moving the left pointer to its right by 1
# if the character pointed by l is in t and window[s[l]]<t_counter[s[l]], the we have an invalid window
# then we need to decrease the available by 1




class Solution:
    def minWindow(self, s: str, t: str) -> str:

        
        window = defaultdict(int)
        t_counter = Counter(t)
        l = 0
        req = len(t_counter)
        avail = 0
        ans = float("infinity")
        res = [-1,-1]
        
      

        for r in range(len(s)):
            c = s[r]
            window[c]+=1
            if c in t_counter and t_counter[c] == window[c]:
                avail+=1
            
            while avail == req:
                if ans > (r-l)+1:
                    ans = (r-l)+1
                    res = [l,r]
                
                window[s[l]]-=1
                if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
                    avail-=1
                l+=1
        print(res)
        l,r = res
        return s[l:r+1] if ans!=float("infinity") else ""