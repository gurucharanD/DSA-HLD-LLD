# start = [1,3,0,5,8,5]
# end = [2,4,6,7,9,9]

# to maximise the number of meetings that could be perfomed
# in a single room, we can choose the meetings that end soon
# and perfrom them first 

start = [10, 12, 20]
end = [20, 25, 30]

meetings = [ [x[0],x[1]] for x in zip(start,end)]
print(meetings)

meetings.sort(key = lambda x:x[1])
currentEndTime = meetings[0][1]
count = 1
start = 0
end = 1

for meet in meetings:
    if meet[start] > currentEndTime:
        currentEndTime = meet[end]
        count+=1

print(count)

