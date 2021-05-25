class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if mid == nums[mid]: i = mid + 1
            else: j = mid - 1
        return i
