nums = [3,2,4]
target = 6
#brute force approach
def Twosum(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
print(Twosum(nums))
#opyimal approach
def function(nums):
    hashing={}
    for i,num in enumerate(nums):
        compliment=target-num
        if compliment in hashing:
            return [hashing[compliment],i]
        else:
            hashing[num]=i
print(function(nums))
'''tracing
hashing={}
when we apply enumeration the (i,num) pairs are (0,3),(1,2),(2,4)
first iteration----i=0 num=3 compliment=6-3 compliment=3 3 is not in hashing
so hashing[3]=0 we have to store key as the num and value as the index of the num so hashing={'3':'0'}
second iteration ----i=1 num=2 compliment=6-2 compliment=4  4 is not in hashing
so hashing[2]=1 hashing={'3':'0','2':'1'}
third iteration --- i=2 num=4 compliment=6-4=2 2 is present in compliment so the pair is formed whose sum is the target
so we have to return the indices of compliment and the num return [hashing[compliment],i]
[hashing[2],2]=[1,2]'''
#<------Two sum on sorted arrays------->
#when ever there is a sorted array we can apply two pointers approach
arr=[2,3,4,5,6]
target=6
def sorted(arr):
    left,right=0,len(arr)-1
    while left<right:
        s1=arr[left]+arr[right]
        if s1==target:
            return [left,right]
        elif s1<target:
            left+=1
        else:
            right-=1
print(sorted(arr))
#the time complixity is o(n)
#the space complexity is o(1)
#keytakeaway:when we are working with the index and the value in any sequence data type using enumeration is best way
#when ever there is a sorted list we have to apply two pointers
