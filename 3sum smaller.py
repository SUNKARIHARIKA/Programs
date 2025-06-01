nums = [-1, 0, 2, 3]
target = 3
nums.sort()
result=[]
count=0
for i in range(len(nums)):
    j,k=i+1,len(nums)-1
    while j<k:
        s1=nums[i]+nums[j]+nums[k]
        if s1<target:
            count+=(k-j)
            j+=1
        else:
            k-=1
print(result)
#the time complexity is o(n**2)
#the auxilary space is o(1)
