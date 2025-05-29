nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
s=set(nums[0])
for i in range(1,len(nums)):
    s=s&set(nums[i])
print(sorted(list(s)))
