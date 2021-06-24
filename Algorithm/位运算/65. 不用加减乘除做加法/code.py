class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left, right = [1]*len(a), [1]*len(a)
        for i in range(1, len(a)):
            left[i] = left[i-1] * a[i-1]
            right[len(a)-1-i] = right[len(a)-i] * a[len(a)-i]
        return [a*b for a, b in zip(left, right)]
