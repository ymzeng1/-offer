class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] <= target: i = mid + 1
            else: j = mid - 1
        right = i
        if j >= 0 and nums[j] != target: return 0
        i = 0
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target: i = mid + 1
            else: j = mid - 1
        left = j

        return right - left - 1
