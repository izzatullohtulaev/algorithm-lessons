# def bsort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#             print(nums)
nums = [7,2,5,3,8,4,1,0]
print("length of an array: ",len(nums))
print(list(range(len(nums))))
# bsort(nums)