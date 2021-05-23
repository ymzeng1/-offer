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
