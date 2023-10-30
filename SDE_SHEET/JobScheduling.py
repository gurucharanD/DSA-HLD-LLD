class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        maxDeadLine = 0
        for job in jobs:
            maxDeadLine = max(maxDeadLine, job.deadline)
        # maxDeadLine tells us the number of days
        # we have to finish all jobs
        
        slots = [-1]*(maxDeadLine+1)
        profit = 0
        count = 0
        jobs.sort(key = lambda x:x.profit, reverse=True)
        
        for job in jobs:
            # reason for looping backwards, is we try to perform
            # everyjob close to its last day because we get time to
            # perform other jobs with closer deadlines 
            for slot in range(job.deadline,0,-1):
                if slots[slot] == -1:
                    profit+=job.profit
                    count+=1
                    slots[slot] = job.id
                    break
                
        return [count,profit]