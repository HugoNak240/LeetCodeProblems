
def sortedSquares(nums):
    for i in nums:
        sqNums = i*i
        indexNums = nums.index(i)
        nums[indexNums] = sqNums
    nums.sort()
    return print(nums)


# Testcase 1
nums = [-4, -1, 0, 3, 10]

# Testcase 2
# nums = [-2, 2, -2, 2, -2]

# Testcase 3
# nums = [8, -4, 3, 0, -5]

sortedSquares(nums)
