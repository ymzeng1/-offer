class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 求和公式
        l, r = 1, 2
        res = []
        while l < r:
            s = (l+r)*(r-l+1)/2
            if s < target: r += 1
            elif s > target: l += 1
            else: 
                res.append([i for i in range(l, r+1)])
                l += 1
        return res
