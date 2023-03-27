class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif not len(nums)-1:
            return -1 if nums[0] != target else 0
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1