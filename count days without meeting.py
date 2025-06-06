'''You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). 
You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap.'''
days = 10
meetings = [[5,7],[1,3],[9,10]]
meetings.sort()
result=[meetings[0]]
for i in range(1,len(meetings)):
    last=result[-1]
    if last[-1]>=meetings[i][0]:
        last[-1]=max(last[-1],meetings[i][-1])
    else:
        result.append(meetings[i])
count=0
for i in range(len(result)):
    count=count+(result[i][1]-result[i][0])+1
print(days-count)