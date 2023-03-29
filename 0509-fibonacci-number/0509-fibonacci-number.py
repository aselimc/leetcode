class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            first, second, i = 0, 1, 0
            while i < n-1:
                answer = first + second
                first = second
                second = answer
                i += 1
            return answer
