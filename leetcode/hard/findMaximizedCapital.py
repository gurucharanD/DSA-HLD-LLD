# sort the projects by the capital in increasing order 
# because, we are constrained by the capital we have in hand
# to choose a project of our choice

# use a pointer and add all the projects that are
# possible with current capital into a max heap by 
# profit and keep incrementing the pointer
# stop when you arrive at a project that is not
# possible to handle with available capital
# at this point we need more capital
# so, we pop the maximum profit that we gained
# by popping the element at the top of our max heap
# and add it to our capital

# with the increased capital we try to find the next possible
# project and repeat the process until k projects are handled
# or there are no more projects that can be handled
# or the max heap is empty (which means there are no more handleable projects)






class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        n = len(profits)
        projects = [(capital[i],profits[i]) for i in range(n)]
        projects.sort()
                
        ptr = 0
        q = []
        
        for _ in range(k):
            
            while ptr < n and w >= projects[ptr][0]:
                
                heappush(q,-projects[ptr][1])
                ptr+=1
            
            if not q:
                break
            
            w += - heappop(q)
        
        return w