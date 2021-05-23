# 自己的做法，设定边界
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        r, c = len(matrix), len(matrix[0])
        # i, j = 0, len()
        n = 0
        self.res = []
        def recur(n):
            self.res += matrix[n][n : c-n]
            if r-n-1 - n >= 2:
                for i in range(n+1, r-n-1):
                    self.res.append(matrix[i][c-n-1])
            if r-n-1 - n >= 1:
                self.res += matrix[r - 1 - n][n:c-n][::-1]
                if n != c - 1 -n:
                    for i in range(r-n-2, n, -1):
                        self.res.append(matrix[i][n])
        
        while len(self.res) != r*c:
            recur(n)
            n += 1
            
        return self.res
    
    
    
 # 逻辑清晰版本， 上下左右四个指标
class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res


