#better solution for finding unique in duplicates
arr=[1,1,2,3,3,4,4]
m=max(arr)
hashing=[0]*(m+1)
for i in arr:  #o(n)
    hashing[i]+=1
print(hashing)
for i in range(len(hashing)):  #o(m)
    if hashing[i]==1:
        print(i)
#the time complexity => o(n+m)
#the space complexity is =>o(m)
#*****whenever the array elements are positive use the hashing technique and when they are negative use map or dictionary data structure
#<------optimal solution---->
xor=0
for i in arr:
    xor=xor^i
print(xor)
#the time complexity =>o(n)
#space complexity=>o(1)