class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #Dynamic Programming with Time Complexity O(n) and Space Complexity O(1)
        # In classic maximum sum subarray, we only track one value (current max sum)
        # But for products, that's not enough because:
        #   Negative * Negative = Positive
        #   Very Small (negative) product can suddenly become the maximum after multiplying by another negative
        # At every index, track curMax (max product at index); curMin (min product ending at index)

        res = max(nums)  #initializing res with max value of array
        curMin, curMax = 1, 1

        for num in nums:
            #Check if num is 0, then reset min max to 1, 1
            if num == 0:
                curMin, curMax = 1, 1
                continue

            tmp = curMax * num
            #Update curMin and curMax, res at every iteration
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num) #not to use modified curMax
            res = max(curMax, res)

        return res