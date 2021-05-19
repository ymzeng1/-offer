#回溯法，自己写的效率低的解
class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()
        visited = [0 for _ in range(len(s))]
        def dfs(temp):
            if len(temp) == len(s):
                res.add(temp)
            for i in range(len(s)):
                if visited[i] == 1:
                    continue
                visited[i] = 1
                dfs(temp+s[i])
                visited[i] = 0
                
        dfs('')
        return list(res)
