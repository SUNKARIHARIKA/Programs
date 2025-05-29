arr = [1, 2, 3, 4, 5, 6, 6]
target = 6
cnt=0
for i in arr:
    if i==target:
        cnt+=1
    else:
        cnt-=1
cnt1=0
for i in range(len(arr)):
    if arr[i]==target:
        cnt1+=1
if cnt>0 and cnt1>len(arr)//2:
    print('True')
else:
    print('False')