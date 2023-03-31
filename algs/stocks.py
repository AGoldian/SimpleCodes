prices = [2, 4, 1]

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        left = 0 
        right = 1

        while right < len(prices):

            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)

            else:
                left = right
            
            right += 1

        return max_profit

print(Solution().maxProfit(prices))