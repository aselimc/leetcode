class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            first, second, i = 0, 1, 0
            while i < n-1:
                answer = first + second #1  #2 #3
                first = second          # 1 #1 #2
                second = answer         # 1 #2 #3
                i += 1
            return answer
