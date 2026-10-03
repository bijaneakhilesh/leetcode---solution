class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        if len(prices) == 1:
            return 0

        curr = prices[0]
        profit = 0

        for i in range(1, len(prices)):

            # If today's price is higher,
            # take the difference as profit.
            if prices[i] > curr:
                profit += prices[i] - curr

            # Move to the next day
            curr = prices[i]

        return profit