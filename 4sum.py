#brute force approach
nums = [1,0,-1,0,-2,2]
target = 0
s=set()
l1=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            for l in range(k+1,len(nums)):
                s1=nums[i]+nums[j]+nums[k]+nums[l]
                if s1==target:
                    s.add(tuple(sorted([nums[i],nums[j],nums[k],nums[l]])))
for i in s:
    l1.append(list(i))
print(l1)
#the time complexity of brute force approach is o(n**4) so we have to reduce to o(n**3)
#better approach
result=set()
l1=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        seen=set()
        for k in range(j+1,len(nums)):
            l=target-(nums[i]+nums[j]+nums[k])
            if l in seen:
                result.add(tuple(sorted([nums[i],nums[j],nums[k],l])))
            seen.add(nums[k])
for i in result:
    l1.append(list(i))
print(l1)
#the time complexity of better solution is o(n**3) so we have to reduce to o(n**2)
#optimal approach
nums.sort()
l1=[]
for i in range(len(nums)):
    if (i>0 and nums[i]==nums[i-1]):
        continue
    for j in range(i+1,len(nums)):
        if j!=i+1 and nums[j]==nums[j-1]:
            continue
        k,l=j+1,len(nums)-1
        while k<l:
            s1=nums[i]+nums[j]+nums[k]+nums[l]
            if s1==target:
                l1.append([nums[i],nums[j],nums[k],nums[l]])
                k+=1
                l-=1
                while(k<l and nums[k]==nums[k-1]):
                    k+=1
                while(k<l and nums[l]==nums[l+1]):
                    l-=1
            elif s1<target:
                k+=1
            else:
                l-=1
print(l1)
             

