arr=[3,2,1,5,2]
#brute force approach
#the time complexity of the above brute force approach is o(nlogn) space complexity is o(1)
arr.sort(reverse=True)
print(arr[0])
#better approach
#the time complexity of the better approach is o(nlogn) and space complexity is o(1)
maximum=float('-inf')
for i in arr:
    if i>maximum:
        maximum=i
print(maximum)
#using buitin function
print(max(arr))
