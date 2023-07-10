def linear_search(list, target):
    for n in range(len(list)):
        if list[n]==target:
            return n
    return None
def binary_search(list, target):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        if list[mid]==target:
            return mid
        elif list[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return None
myList1 = [1,3,4,6,7,8,10, 12, 23, 45, 56, 78, 99]

# print(linear_search(myList1, 11))
# print(binary_search(myList1, 11))


mevalar = ['olma', 'behi', 'anor', 'olcha', 'shaftoli', 'anjir']
mevalar.sort()
print(mevalar)
print(binary_search(mevalar, 'behi'))