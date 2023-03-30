class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums)-1
        answer = []
        while low<=high:
            h = nums[high] ** 2
            l = nums[low] ** 2
            if l < h:
                answer.append(h)
                high -= 1
            else:
                answer.append(l)
                low +=1
        return list(reversed(answer))