# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
#  all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

# !!! Don't have access to API from here, so this code doesn't work !!!

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(self, n: int) -> int:
    left = 0
    right = n-1
    while(left <= right):
        mid = floor(left-(left-right)/2)
        if(isBadVersion(mid)):

            if not isBadVersion(mid-1):
                return mid
            else:
                right = mid-1
        else:
            if isBadVersion(mid+1):
                return mid+1
            else:
                left = mid+1

    return -1
