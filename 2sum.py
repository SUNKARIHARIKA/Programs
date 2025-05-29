nums = [3,2,4]
target = 6
hashing={}
l=[]
for i,num in enumerate(nums):
    compliment=target-num
    if compliment in hashing:
        l.append([hashing[compliment],i])
    hashing[num]=i
print(l)
