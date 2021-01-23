def findValueSortedShiftedArray(nums, target):
    def binarySearch(target, left, right):
        if (left > right):
            return - 1
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return binarySearch(target, mid + 1, right)
        else:
            return binarySearch(target, left, mid - 1)
    
    if target >= nums[0]:
        return binarySearch(target, 0, nums[0])
    else:
        return binarySearch(target, nums[0], len(nums) -1)
        

