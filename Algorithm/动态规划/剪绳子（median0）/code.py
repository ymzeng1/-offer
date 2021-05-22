class Solution:
    def cuttingRope(self, n: int) -> int:
        # # 动态规划
        # dp = [0]*(n+1) # dp[n] = 长度为n的绳子最大的乘积
        # dp[2] = 1
        # for i in range(3, n+1):
        #     for j in range(2, i):
        #         dp[i] = max(dp[i], max(j*dp[i-j], j*(i-j)))
        # return dp[n]

        #贪心思想
        if n <= 3: return n - 1
        if n % 3 == 0: return int(3**(n / 3))
        elif n % 3 == 1: return int(3**((n-4) / 3) * 4)
        else: return int(3**((n - 2) / 3) * 2)
