# 大部分都还没理解透
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j):
            if i == 0: return False
            if p[j - 1] == '.': return True
            return s[i-1] == p[j-1]
        
        m, n = len(s), len(p)
        f = [[False]*(n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j-2]
                    if match(i, j-1):
                        f[i][j] |= f[i-1][j]
                else:
                    if match(i, j):
                        f[i][j] |= f[i-1][j-1]
        return f[m][n]
      
      
 # 相似好理解解法     
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s) + 1, len(p) + 1
        dp = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                # 分成空正则和非空正则两种
                if j == 0:
                    dp[i][j] = i == 0
                else:
                    # 非空正则分为两种情况 * 和 非*
                    if p[j-1] != '*':
                        if i>0 and (s[i-1] == p[j-1] or p[j-1] == "."):
                            dp[i][j] = dp[i-1][j-1]
                    else:
                        # 碰到 * 了，分为看和不看两种情况
                        # 不看
                        if j >= 2:
                            dp[i][j] |= dp[i][j - 2]
                        # 看
                        if i >= 1 and j >= 2 and (s[i-1]==p[j-2] or p[j-2] == "."):
                            dp[i][j] |= dp[i - 1][j]
        return dp[n-1][m-1]
