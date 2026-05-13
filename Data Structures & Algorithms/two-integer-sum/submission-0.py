class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Option1 : Hashmap(Dictionaries); Time/Space Complexity O(n)

        prevMap = {} #Empty Hashmap to store val:index pair

        for i, n in enumerate(nums):
            diff = target - n #calculate difference
            if diff in prevMap: #check if difference in hashmap, if there return pair of diff's index and n's index i.e. i
                return [prevMap[diff], i]
            prevMap[n] = i #else store index in hashmap as val:index

        return #As function requires return so default return statement
        
        # # Option2 : Brute Force (Using 2 arrays); Time Complexity O(n^2) and Space Complexity O(1)
        # for i in range(len(nums)): #i from start to end
        #     for j in range(i+1, len(nums)): #j from i+1 to end
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         pass
        #     pass
        
        # return #As function requires return so default return statement