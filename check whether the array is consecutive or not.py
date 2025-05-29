#Determine whether the elements of a given array form a sequence of consecutive integers. The sequence can be in any order but must 
# contain every integer between the minimum and maximum values exactly once (no duplicates, no missing numbers)
arr=[1, 2,3, 4, 5,6]
#Explanation: The array contains all integers from 2 to 6 with no missing numbers or duplicates. The consecutive sequence is 
# [2, 3, 4, 5, 6].
#brute force approach
arr.sort()
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]+1:
        print('false')
        break
else:
    print('True')
#the time complexity of the above brute force is o(nlogn)+o(m)
#better approach(hashing)
minimum=min(arr)
maximum=max(arr)
hashing=[0]*(maximum+1)
for i in arr:  #o(n)
    hashing[i]+=1
for i in range(minimum,maximum+1):  #o(n)
    if hashing[i]!=0:
        print('False')
        break
else:
    print('True')
#the time complexity is o(2n)
#the spac complexity is o(n)
#optimal approach
s=set(arr)
minimum=min(s)
maximum=max(s)
print(len(s)==(maximum-minimum)+1)


