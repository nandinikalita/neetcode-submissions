class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Using hashmap : Time complexity O(n); Space complexity O(n)
        prevMap = {} #Value-index pair

        for i, n in enumerate(nums):
            if n in prevMap: #Check if n is present in prevMap (duplicate), then return True
                return True
            else:
                prevMap[n] = i #Else store n in prevMap as n, i pair
        
        return False