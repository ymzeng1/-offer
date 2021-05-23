  class Solution:
    def exchange(self, nums: List[int]) -> List[int]:      
        if not nums: return []
        a, b = 0, len(nums) - 1
        while a < b:
            if nums[a] % 2 == 1:
                a += 1
                continue
            if nums[b] % 2 == 0:
                b -= 1
                continue
            nums[a], nums[b] = nums[b], nums[a]
        return nums
