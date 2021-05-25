# 双指针 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic: i = max(i, dic[s[j]])
            dic[s[j]] = j
            res = max(res, j - i)
        return res
      
      
# 动态规划 + 哈希表
