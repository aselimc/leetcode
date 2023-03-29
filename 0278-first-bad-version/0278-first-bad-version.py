# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        memory = {}
        flag = True
        while flag:
            mid = (low + high) // 2
            if mid in memory:
                bad = memory[mid]
            else:
                bad = isBadVersion(mid)
            if mid-1 in memory:
                good = memory[mid-1]
            else:
                good = isBadVersion(mid-1)
            memory[mid] = bad
            memory[mid-1] = good
            if bad and not good:
                return mid
            elif bad and good:
                high = mid -1
            else:
                low = mid + 1