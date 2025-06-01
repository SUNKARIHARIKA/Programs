nums = [-1,2,1,-4]
target = 1
#brute force approach
m=float('inf')
triplet=[0]*3
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            s1=abs((nums[i]+nums[j]+nums[k])-target)
            if m>s1:
                m=s1
                triplet=[nums[i],nums[j],nums[k]]
print(sum(triplet))
#optimal solution
nums.sort()
l=[]
m=float('inf')
triplet=[0]*3
for i in range(len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    j,k=i+1,len(nums)-1
    while j<k:
        s1=nums[i]+nums[j]+nums[k]
        if abs(s1-target)<m:
            m=abs(s1-target)
            triplet=[nums[i],nums[j],nums[k]]
        if s1<target:
            j+=1
        elif s1>target:
            k-=1
        else:
            print(sum(triplet))
print(sum(triplet))


            
            