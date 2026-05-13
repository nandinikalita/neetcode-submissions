class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # #Using hashmap : Time complexity O(n); Space complexity O(n)
        # prevMap = {} #Value-index pair

        # for i, n in enumerate(nums):
        #     if n in prevMap: #Check if n is present in prevMap (duplicate), then return True
        #         return True
        #     else:
        #         prevMap[n] = i #Else store n in prevMap as n, i pair
        # return False

        #OR Sort array : better Space Complexity but low Time Complexity
        # Sorting increases Time Complexity to O(nlogn), Space Complexity = O(1)

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False