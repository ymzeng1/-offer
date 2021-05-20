class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[-1] <= 0: dp.append(num)
            else: dp.append(dp[-1] + num)
        return max(dp)
