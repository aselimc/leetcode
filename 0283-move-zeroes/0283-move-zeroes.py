class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        it, zero_counter, n = 0, 0, len(nums)
        while it < n:
            if nums[it] == 0:
                zero_counter += 1
            else:
                nums[it-zero_counter] = nums[it]
            it += 1
        it = 0
        while it<zero_counter:
            nums[n-it-1] = 0
            it += 1