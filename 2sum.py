nums = [3,2,4]
target = 6
#brute force approach
def Twosum(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
print(Twosum(nums))
#the time complexity of the brute force approach is o(n**2)
#the space complexity is o(1)
#opyimal approach
hashing={}
l=[]
for i,num in enumerate(nums):
    compliment=target-num
    if compliment in hashing:
        l.append([hashing[compliment],i])
    hashing[num]=i
print(l)
#keytakeaway:when we are working with the index and the value in any sequence data type using enumeration is best way
