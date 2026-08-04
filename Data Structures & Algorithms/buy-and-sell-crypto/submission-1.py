class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit = 0
        minimum_buy = prices[0]

        for sell in prices:
            maximum_profit = max(maximum_profit, sell - minimum_buy)
            minimum_buy = min(minimum_buy, sell)
        return maximum_profit