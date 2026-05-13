class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Two Pointer array : Time Complexity O(n); Space Complexity O(1)

        #Using left and right pointer to traverse through the array
        l, r = 0, 1 #Left pointer is Buy, Right pointer is Sell
        maxProfit = 0 #Maximum Profit

        #We buy at the lowest and Sell at the highest
        while r < len(prices):

            if prices[l] < prices[r]: #In this case, l<r then calc profit
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)  #Update MaxProfit for highest profit
            else:
                l = r # if l>r, then move l to r position to get lowest price to buy
            
            r += 1 #everytime increment r by 1

        return maxProfit