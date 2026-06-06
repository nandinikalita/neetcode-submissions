class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #Using first sorting array and two pointers; Time Complexity=O(nlogn)+O(n2) ie O(n2); Space Complexity=O(1)
        res = []   #List of triplets

        #Sort the array
        nums.sort()

        #Initialize two pointers
        l, r = 0, len(nums) - 1

        
        #Loop through first value
        for i, a in enumerate(nums):
            #Check if first value and next value is same, then skip the duplicate
            if a == nums[i-1] and i > 0:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                ThreeSum = a + nums[l] + nums[r]

                if ThreeSum > 0:
                    r -= 1
                elif ThreeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #Move l pointer to next elt to capture next triplet
                    l += 1
                    #Check if l_value is duplicate, the increment l pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res