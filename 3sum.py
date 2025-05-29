nums = [-1,0,1,2,-1,-4]
#brute force approach
s=set()
l1=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if(nums[i]+nums[j]+nums[k]==0):
                s.add(tuple(sorted([nums[i],nums[j],nums[k]])))
for i in s:
    l1.append(list(i))
print(l1)
#the time complexity for the brute force approach is o(n**3) so we can reduce it to o(n**2) in better solution
#better solution
result=set()
l=[]
for i in range(len(nums)):
    seen=set()
    for j in range(i+1,len(nums)):
        c=-(nums[i]+nums[j])
        if c in seen:
            result.add(tuple(sorted([nums[i],nums[j],c])))
        seen.add(nums[j])
for i in result:
    l.append(list(i))
print(l)
#to reduce the time complexity to o(nlogn)+o(n**2)=>o(n**2) with space complexity=>o(1)
nums.sort()
result=[]
for i in range(len(nums)):
    if(i>0 and nums[i]==nums[i-1]):
        i+=1
    j=i+1
    k=len(nums)-1
    while j<k:
        s1=nums[i]+nums[j]+nums[k]
        if s1<0:
            j+=1
        elif s1>0:
            k-=1
        else:
            result.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while k>j and nums[k]==nums[k+1]:
                k-=1
print(result)




