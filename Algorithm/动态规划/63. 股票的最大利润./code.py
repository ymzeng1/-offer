class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        cost, profit = prices[0], 0
        for price in prices[1:]:
            profit = max(profit, price - cost)
            cost = min(cost, price)
        return profit
