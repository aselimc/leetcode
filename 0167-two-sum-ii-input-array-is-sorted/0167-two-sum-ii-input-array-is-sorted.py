class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right= 0, len(numbers) -1
        left_temp, right_temp = -1001, 1001
        while left<right:
            s = numbers[left] + numbers[right]
            if s==target:
                return [left+1, right+1]
            elif s>target:
                while numbers[right] >= right_temp:
                    right -= 1
                right_temp = numbers[right]
            else:
                while numbers[left] <= left_temp:
                    left += 1
                left_temp = numbers[left]

            
            
            