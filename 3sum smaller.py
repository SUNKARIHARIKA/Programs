nums = [-1, 0, 2, 3]
target = 3
nums.sort()
result=[]
for i in range(len(nums)):
    j,k=i+1,len(nums)-1
    while j<k:
        s1=nums[i]+nums[j]+nums[k]
        if s1>target:
            k-=1
        elif s1==target:
            k-=1
        else:
            result.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
print(result)