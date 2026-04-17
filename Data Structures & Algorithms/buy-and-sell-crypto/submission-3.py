class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n**2)
        # SC: O(1)
        prof = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                prof = max(prof, diff)
        return prof