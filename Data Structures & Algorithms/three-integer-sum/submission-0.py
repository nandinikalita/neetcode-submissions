class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #Using Sort + Two Pointer; Time Complexity = O(nlogn)+O(n2) As O(n2); Space Complexity O(1)
        res = []  #resultant array is list of triplets
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: #if not first elt and equal to prev elt then skip
                continue

            l, r = i+1, len(nums) - 1  #left and right pointers point i+1 and last elt

            while l < r:
                #Compute ThreeSum
                ThreeSum = a + nums[l] + nums[r]

                if ThreeSum > 0:
                    r -= 1
                elif ThreeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])

                    #Everytime move left pointer
                    l += 1

                    #If l points to next elt which is equal to prev elt
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            
        return res

