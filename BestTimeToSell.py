class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        max_profit = 0

        while r < len(prices) :
            if prices[r] < prices[l] : 
                l = r 

            else :  
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            r += 1 
        
        return max_profit
