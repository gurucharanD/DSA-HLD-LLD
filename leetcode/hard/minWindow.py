class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        i = 0
        j = -1
        
        t_counter = Counter(t)
        s_counter = defaultdict(int)

        required = len(t_counter)
        available = 0
        
        answer = ''
        
        while i < len(s):
            #inrement the window
            if available < required:
                
                if j == len(s)-1:
                    return answer
                
                j+=1
    
                s_counter[s[j]] += 1
                if t_counter[s[j]] and t_counter[s[j]] == s_counter[s[j]]:
                    available += 1
                    


            #decrement the window such that the count of s[i] in in s_counter
            #should be less than the count of s[i] in t_counter
            #if the count of s[i] in s_count is already less in t_count
            #dont ado anything            
            else:
                
                s_counter[s[i]] -= 1
                if t_counter[s[i]] and s_counter[s[i]] < t_counter[s[i]]:
                    available -= 1
                
                i+=1
            
            if required == available:
                
                if not answer:
                    answer = s[i:j+1]
                elif (j-i+1) < len(answer):
                    answer = s[i:j+1]
                

        return answer
                
                
        
        