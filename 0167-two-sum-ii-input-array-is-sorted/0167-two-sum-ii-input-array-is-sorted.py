class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = -1001
        for i in range(len(numbers)):
            if numbers[i] <= first:
                continue
            first = numbers[i]
            second = -1001
            for j in range(i+1, len(numbers)):
                if numbers[j] <= second:
                    continue
                second = numbers[j]
                if first+second == target:
                    return [i+1, j+1]