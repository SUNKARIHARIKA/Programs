arr=[1,2,3]
subarrays=[]
for start in range(len(arr)):
    for end in range(start+1,len(arr)):
        subarrays.append(arr[start:end])
print(subarrays)
