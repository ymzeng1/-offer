class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0]*32
        for num in nums:
            for i in range(32):
                counts[i] += num & 1
                num >>= 1
        res, repeat = 0, 3
        
        for j in range(32):
            res <<= 1
            res |= counts[31 - j] % repeat
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff) ## python 存储负数的特殊性
