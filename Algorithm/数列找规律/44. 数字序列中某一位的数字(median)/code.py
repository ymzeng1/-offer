class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count #确认所在的位数
            digit += 1
            start *= 10
            count = 9*digit*start
        num = start + (n-1) // digit #确认哪一个数
        return int(str(num)[(n-1) % digit]) # 确定数中的第几位
