class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1        #l and r are two pointers that show indeces
        maxProfit = 0

        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r     #l is jumping to r's spot
            r += 1
        return maxProfit