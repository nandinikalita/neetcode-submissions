class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Option1 : Using hashmapl; Time complexity O(n)

        #Option2: Using Brute Force approach
        duplicate = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    duplicate += 1
                    return True
                else:
                    pass
                
        return False
        