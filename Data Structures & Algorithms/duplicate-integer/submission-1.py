class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Option1 : (Optimized) Using hashmap; Time complexity O(n); Space Complexity O(n)
        hashMap = set() #Empty hashmap

        for n in nums:
            if n in hashMap:
                return True
            hashMap.add(n)
       
        return False
    
        #Option2: Sort and then parsing through array; Time Complexity O(nlogn); Space Complexity O(1)
        # sorted_nums = sorted(nums)

        # #Check for adjacent items in array, if they are equal
        # n=0
        # while n < (len(sorted_nums)-1):
        #     if sorted_nums[n] == sorted_nums[n+1]:
        #         return True
        #     n += 1
        
        # return False

        #Option3: Using Brute Force approach; Time complexity O(n^2); Space complexity O(1)

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        #         else:
        #             pass
                
        # return False
        