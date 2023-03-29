class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        if high==-1: return 0
        elif target > nums[-1]: return high+1
        elif target < nums[0]: return 0
        else:
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target: return mid
                elif nums[mid] < target: low = mid+1
                else: high = mid-1
            return low