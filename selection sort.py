arr=[13,46,24,52,20,9]
n=len(arr)
for i in range(n-1):
    mini=i
    for j in range(i,n):
        if arr[j]<arr[mini]:
            mini=j
    arr[i],arr[mini]=arr[mini],arr[i]
print(arr)
