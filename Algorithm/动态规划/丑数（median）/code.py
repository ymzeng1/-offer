# 最小堆 + set
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = {1}
        heap = [1]
        for _ in range(n-1):
            cur = heapq.heappop(heap)
            for i in [2, 3, 5]:
                nxt = i * cur
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return heapq.heappop(heap)
      
      
# 动态规划
