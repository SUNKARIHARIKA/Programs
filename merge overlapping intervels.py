arr=[[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
#brute force approach
'''result=[]
n=len(arr)
arr.sort()
for i in range(len(arr)):
    start=arr[i][0]
    end=arr[i][1]
    if result and end<=result[-1][1]:
        continue
    for j in range(i+1,len(arr)):
        if arr[j][0]<=end:
            end=max(end,arr[j][1])
        else:
            break
    result.append([start,end])
print(result)'''
#the time complexity is o(nlogn)+o(2n) where o(nlogn) for sorting the array and o(2n) is we are iterating each element at 2 times
n=len(arr)
arr.sort()
result=[arr[0]]
for i in range(1,len(arr)):
    last=result[-1]
    if arr[i][0]<=last[1]:
        last[1]=max(arr[i][1],last[1])
    else:
        result.append(arr[i])
print(result)

