class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        max_profit = 0

        for curr in prices:
            if curr < buy:
                buy = curr
            else:
                max_profit = max(max_profit, curr - buy)
        return max_profit