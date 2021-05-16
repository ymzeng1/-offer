# 深度优先遍历（DFS）
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def numsum(i):
            sumi = 0
            while i:
                sumi += (i%10)
                i = i//10
            return sumi

        def detect(i, j):
            if i<0 or j<0 or i>=m or j>=n or (numsum(i) + numsum(j)) > k or (i, j) in loc: return 0
            loc.add((i, j))
            return 1 + detect(i-1, j) + detect(i+1, j) + detect(i, j-1) + detect(i, j+1)
        
        loc = set()
        return detect(0, 0)
      
# 广度优先遍历（BFS）
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i,j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)

