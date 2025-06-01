'''
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j,
nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''
arr=[1,2,3,4,5,0]
is_increasing=True
is_decreasing=True
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        is_decreasing=False
    else:
        is_increasing=False
if is_increasing or is_decreasing:
    print('True')
else:
    print('False')