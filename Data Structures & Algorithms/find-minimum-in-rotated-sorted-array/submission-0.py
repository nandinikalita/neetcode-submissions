class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #Binary search
        res = nums[0]

        #Left Right pointer
        l , r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            #Compute medium value
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1 #Search Right
            else:
                r = m -1 #Search Left
            
        return res

