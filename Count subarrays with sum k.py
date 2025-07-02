arr=[1,2,3,-3,1,1,1,4,2,-3]
k=3
#brute force approach -(do by generating all subarrays)
n=len(arr)
count=0
for i in range(n):
    for j in range(i,n):
        s1=0
        for l in range(i,j+1):
            s1=s1+arr[l]
        if s1==k:
            count+=1
print(count)
#the time complexity is o(n**3)
#the space complexity is o(1)
#better solution
count1=0
for i in range(n):
    s2=0
    for j in range(i,n):
        s2=s2+arr[j]
        if s2==k:
            count1+=1
print(count1)
#the time complexity is o(n**2)
#the space complexity is o(1)
#optimal approach(using hashing)
hashing={0:1}
count2=0
prefix_sum=0
for i in range(len(arr)):
    prefix_sum=prefix_sum+arr[i]
    if prefix_sum-k in hashing:
        count2+=hashing[prefix_sum-k]
    if prefix_sum in hashing:
        hashing[prefix_sum]+=1
    else:
        hashing[prefix_sum]=1
print(count2)

