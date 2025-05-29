arr=[1,1,4,4,5,5,6]  # we have to modify the array without using extra space
#brute force approach
#the time complexity for insertion of elements in python is o(n) where as in c++/java it is o(nlogn)
s=set()
for i in arr:
    s.add(i)
print(s)
print(len(s))
#optimal approach(two pointer)
start=1
for i in range(1,len(arr)):
    if arr[i]!=arr[start-1]:
        arr[start]=arr[i]
        start+=1
print(arr)
print("the number of unique elements in array is",start)
