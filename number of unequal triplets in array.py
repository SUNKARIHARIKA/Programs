nums = [4,4,2,4,3]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            continue
        for k in range(j+1,len(nums)):
            if nums[i]!=nums[k] and nums[j]!=nums[k]:
                count+=1
print(count)