# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low+(high-low) // 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low
