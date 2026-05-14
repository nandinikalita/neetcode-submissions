class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = nums[0]  #initializing max sum of subarray to first elt value
        curSum = 0

        for i in nums:
            if curSum < 0: #if curSum drops below 0, reset it to 0 and start with new subarray with next elt
                curSum = 0

            curSum += i #Add next elt to the sum
            maxSub = max(maxSub, curSum)  #maximum of curSum or maxSub
            
        return maxSub
