# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = []
        i = j = len(s) - 1
        while i>=0:
            while i >= 0 and s[i] != ' ': i -= 1
            res.append(s[i+1: j+1])
            while s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)



# 分割+倒序 （使用库函数）
class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.strip().split()[::-1]
        res = ' '.join(tmp)
        return res
