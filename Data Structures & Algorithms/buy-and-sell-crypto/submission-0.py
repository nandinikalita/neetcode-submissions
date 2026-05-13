class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Option1 : Brute Force Approach; Time complexity O(n^2); Space complexity O(1)

        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]  #Calculate profit
                if profit > maxProfit:
                        maxProfit = profit #Store maximum profit
                        # print(maxProfit)

        return maxProfit