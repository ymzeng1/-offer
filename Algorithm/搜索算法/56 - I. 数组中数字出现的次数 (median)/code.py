class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while ret & div == 0:
            div <<= 1
        a, b = 0, 0
        for i in nums:
            if div & i:
                a ^= i
            else: b ^= i
        return [a, b]
