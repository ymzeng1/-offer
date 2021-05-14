# 自己硬解 （时间复杂度高）
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        while nums and i<=len(nums)-k:
            res.append(max(nums[i:i+k]))
            i += 1
        return res

    
        # 单调队列（单调递减）    
        if not nums: return []   
        res = []
        queue = collections.deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]: queue.pop() # 删除所有比num[i]小的数
            queue.append(nums[i])
        res.append(queue[0])
        for i in range(k, len(nums)):
            if nums[i-k] == queue[0]: queue.popleft()
            while queue and queue[-1] < nums[i]: queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        return res
