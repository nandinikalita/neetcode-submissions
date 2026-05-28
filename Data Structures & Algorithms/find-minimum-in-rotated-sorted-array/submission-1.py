class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #Using Binary Search for optimal solution to determmine which half contains the minimum
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #Check if l to r is sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l]) #Minimum of res or nums[l]
                break

            #Medium is computed
            m = (l + r) // 2
            res = min(res, nums[m])

            #Check if left array is sorted -> search right
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1 #Search left array

        return res