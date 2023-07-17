from random import randrange
def qsort(nums):
    if len(nums)<2:
        return nums
    pivot = nums.pop(randrange(len(nums)))
    kichik = [i for i in nums if i<=pivot]
    katta = [i for i in nums if i>pivot]
    return qsort(kichik)+[pivot]+qsort(katta) 