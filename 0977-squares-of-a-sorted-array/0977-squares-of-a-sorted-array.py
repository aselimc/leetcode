class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums)-1
        answer = []
        while low<=high:
            if abs(nums[low]) < abs(nums[high]):
                answer.insert(0, nums[high]**2)
                high -= 1
            else:
                answer.insert(0, nums[low]**2)
                low +=1
        return answer