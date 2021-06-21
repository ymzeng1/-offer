class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1/6]*6
        for k in range(2, n+1):
            tmp = [0] * (5*k + 1)
            for i in range(len(dp)):
                for j in range(6):
                    tmp[j + i] += dp[i]/6
            dp = tmp
        return dp
