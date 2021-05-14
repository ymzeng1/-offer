# 自己硬解 （时间复杂度高）
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        while nums and i<=len(nums)-k:
            res.append(max(nums[i:i+k]))
            i += 1
        return res
