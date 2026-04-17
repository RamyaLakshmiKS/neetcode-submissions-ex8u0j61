class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        l = 0
        prof = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                prof = max(prof, (prices[r] - prices[l]))
        return prof