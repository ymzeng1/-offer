class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            if i not in dic: dic[i] = 1
            else: dic[i] += 1
        for i in s:
            if dic[i] == 1: return i
        return " "
      
      
# 优化
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '
