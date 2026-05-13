class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hashmap

        #Create hashmap i.e. value-index pair
        prevMap = {}  #value-index pair

        # Go through the array, check if target-num is present in HashMap
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            # Else Store the value-index pair in HashMap
            prevMap[n] = i
            

            #Time complexity is O(n)
