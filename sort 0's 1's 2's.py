arr=[0,1,2,0,1,2,0,1,2]
#brute foce approch
'''arr.sort()
print(arr)
#the time complexity of the above brute force approah is o(nlogn)
#the space complexity/auxilary is o(1)
#better solution(hashing)
cnt0=0
cnt1=0
cnt2=0
for i in arr:
    if i==0:
        cnt0+=1
    elif i==1:
        cnt1+=1
    else:
        cnt2+=1
index=0
for i in range(cnt0):
    arr[index]=0
    index+=1
for i in range(cnt1):
    arr[index]=1
    index+=1
for i in range(cnt2):
    arr[index]=2
    index+=1
print(arr)'''
#the time complexity of the better solution is o(n)
#the extra/auxilary space is o(1)
#<-----optimal approach----->
low=0
mid=0
high=len(arr)-1
while mid<=high:
    if arr[mid]==1:
        mid+=1
    elif arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        mid+=1
        low+=1
    else:
        arr[high],arr[mid]=arr[mid],arr[high]
        high-=1
print(arr)

