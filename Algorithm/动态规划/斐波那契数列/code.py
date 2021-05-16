class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            sum = a + b
            a = b
            b = sum
        return a % 1000000007
