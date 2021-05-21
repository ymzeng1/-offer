class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 暴力解法
        # res = 0
        # if len(nums) <= 1: return res
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]: res += 1
        # return res
  
        # 归并排序
        def merge(nums, tmp, l, r):
            if l >= r: return 0
            mid = (l + r) // 2
            inv_count = merge(nums, tmp, l, mid) + merge(nums, tmp, mid + 1, r)
            i, j, pos = l, mid + 1, l

            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    tmp[pos] = nums[i]
                    i += 1
                    # inv_count += (j - (mid + 1))
                else:
                    tmp[pos] = nums[j]
                    j += 1
                    inv_count += (mid - i + 1)
                pos += 1
            for k in range(i, mid + 1):
                tmp[pos] = nums[k]
                # inv_count += (j - (mid + 1))
                pos += 1
            for k in range(j, r + 1):
                tmp[pos] = nums[k]
                inv_count += (mid - i + 1)
                pos += 1
            nums[l:r+1] = tmp[l:r+1]
            return inv_count
            
        
        n = len(nums)
        tmp = [0] * n
        return merge(nums, tmp, 0, n - 1)
