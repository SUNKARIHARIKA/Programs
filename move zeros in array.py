#brute force approach
arr=[1,0,2,3,2,0,0,4,5,1]
temp=[]
for i in range(len(arr)):  #o(n)
    if arr[i]!=0:
        temp.append(arr[i])
nonzero=len(temp)
for i in range(len(temp)):   #o(x) where x is the number of nonzero elements
    arr[i]=temp[i]
print(arr)
for i in range(nonzero,len(arr)):  #o(n-x)
    arr[i]=0
print(arr)
#the total time complexity is =>o(n)+o(x)+o(n-x)=>o(2n)
#the space complexity is o(x) in worst case o(n)
#optimal approach
start=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[start]=arr[i]
        start+=1
for i in range(start,len(arr)):
    arr[i]=0
print(arr)
