class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh = []
        self.maxh = []


    def addNum(self, num: int) -> None:
        if len(self.minh) == len(self.maxh):
            heapq.heappush(self.minh, -heapq.heappushpop(self.maxh, -num))
        else:
            heapq.heappush(self.maxh, -heapq.heappushpop(self.minh, num))


    def findMedian(self) -> float:
        if len(self.minh) != len(self.maxh):
            return self.minh[0]
        else: 
            return (self.minh[0] - self.maxh[0]) / 2.0
