#brute force approach
'''arr=[1,2,3,4,5]
k=3
longest=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        current_sum=0
        for l in range(i,j+1):
            current_sum+=arr[l]
        if current_sum==k:
            longest=max(longest,j-i+1)
print(longest)
#the time complexity of the above approach is=>o(n**3)
#the space complexity is o(1)
#<----better approach---->
longest=0
for i in range(len(arr)):
    current_sum=0
    for j in range(i,len(arr)):
        current_sum+=arr[j]
        if current_sum==k:
            longest=max(longest,j-i+1)
print(longest)'''
#the time complexity is o(n**2)
#the space complexity is o(1)
#optimal approach
arr=[1,2,3,1,1,1,1,3,3]
k=6
left,right=0,0
maxlen=0
current_sum=0
while right<len(arr):
    current_sum=current_sum+arr[right]
    right+=1
    while left<=right and current_sum>k:
        current_sum-=arr[left]
        left+=1
    if current_sum==k:
        maxlen=max(maxlen,right-left)
print(maxlen)
    

