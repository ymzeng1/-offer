class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in dic: 
                stack.append(i)
            else:
                if stack and dic[stack[-1]] == i: stack.pop()
                else: return False
        return False if stack else True
