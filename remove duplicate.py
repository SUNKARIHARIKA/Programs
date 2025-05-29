nums = [0,0,1,1,1,2,2,3,3,4]
start=1
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]:
        nums[start]=nums[i]
        start+=1
print(start)

