class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Option1 : Brute Force Approach; Time complexity O(n^2); Space complexity O(1)

        # maxProfit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]  #Calculate profit
        #         if profit > maxProfit:
        #                 maxProfit = profit #Store maximum profit
        #                 # print(maxProfit)

        # return maxProfit

        #Option2 : Optimized solution; Time Complexity O(n); Space Complexity O(1)

        l,r = 0,1 #(index 0) l=Buy, (index=1) r=Sell
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)  #assigns max profit
            else:
                l = r #shift l to r if prices[l] > prices[r] as we want to buy at lowest and sell at highest
            r += 1 #move r by 1 at every iteration

        return maxProfit