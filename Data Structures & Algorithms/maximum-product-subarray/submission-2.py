class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #Resultant output
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            tmp = n * currMax
            currMax = max(n * currMax, n * currMin, n)  #depending on n being +ve/-ve or currMax/currMin being +ve/-ve
            currMin = min(tmp, n * currMin, n)

            if n == 0:
                currMax = 1
                currMin = 1
                continue
            
            res = max(res, currMax)

        return res