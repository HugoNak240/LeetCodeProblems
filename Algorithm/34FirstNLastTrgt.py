

def searchRange(nums, target):
    low = 0
    up = len(nums)-1
    output = []
    while low <= up:
        mid = (low + up)//2
        print(mid)
        if nums[mid] == target and nums[mid+1] == target:
            output = [mid, mid+1]
            print("1st IF")
            return output
        elif nums[mid] < target:
            low = mid + 1
            print("mid2low")
        elif nums[mid] > target:
            up = mid - 1
            print("mid2high")
        else:
            output = [-1, -1]
            return output
    print("Yo")
    print(output)


# Test case 1, predicted result = [2,3]
nums = [1, 2, 3, 3, 4, 5]
target = 3

# Test case 2, predicted result = [-1,-1]
# nums = [1, 2, 3, 3, 4, 5]
# target = 9

searchRange(nums, target)


found = []


# def first_and_last(nums, target):
#     low = 0
#     high = len(nums)

#     while high >= low:
#         mid = (low + high) // 2
#         if nums[mid] < target:
#             low = mid + 1
#         elif nums[mid] > target:
#             high = mid - 1
#         else:
#             found.append(mid)
#             low = mid + 1
#             if len(found) == 0:
#         found.extend([-1, -1])

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         low = 0
#         up = len(nums) - 1
#         output = [-1,-1]
#         while low<=up:
#             mid =(low +up)//2
#             if nums[mid] == target and nums [mid+1] == target:
#                 output = [mid,mid+1]
#             elif nums[mid]< target:
#                 low = mid + 1
#             else:
#                 up = mid -1
#         return output
