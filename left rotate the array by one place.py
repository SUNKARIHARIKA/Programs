arr=[1,2,3,4,5]
#the output should be [2,3,4,5,1] without taking an extra array that is modifying the input array
#the time complexity of the above approach is o(n) and space complexity is o(1)
'''firstelement=arr[0]
start=0
for i in range(1,len(arr)):
    arr[start]=arr[i]             #we can also solve this without using start variable arr[i]=arr[i-1]
    start+=1
arr[-1]=firstelement
print(arr)
#the space that we are using for this code is o(n) because we are using the input array of size n
#the extra space(auxiliary) that we are using for this code is o(1) because we are not using any extra array or variable other than input
#<------   LEFT ROTATE AN ARRAY BY D PLACES ------->
#---->brute force approach----->
#the time complexity for the above code is o(n+d)
d=int(input("enter the number of places you want to left rotate the array"))
d=d%len(arr)
arr1=arr[:d]   #o(d)
for i in range(d,len(arr)):   #o(n-d)
    arr[i-d]=arr[i]   
for i in range(len(arr)-d,len(arr)):   #o(d)
    arr[i]=arr1[i-(len(arr)-d)]
print(arr)'''
#total time complexity=>o(d)+o(n-d)+o(d)=>o(n+d)
#the extra space/auxiliary space that we are using is o(d)
#---->OPTIMAL APPROACH----->
def reverse(left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
d=int(input("enter the number of positions you want to rotate to left"))
reverse(0,d-1)
reverse(d,len(arr)-1)
reverse(0,len(arr)-1)
print(arr)


