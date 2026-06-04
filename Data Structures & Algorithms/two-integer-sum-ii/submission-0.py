class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Using l, r pointers; Time Complexity O(n); Space Complexity O(1)
        l, r = 0, len(numbers) - 1
        TwoSum = 0

        while l < r:
            TwoSum = numbers[l] + numbers[r]

            if TwoSum < target:
                l = l+1  #Shift left pointer to right, as sorted array, to increase TwoSum 
                            #and bringing close to target
            elif TwoSum > target:
                r = r-1  #Shift Right pointer to left, to decrease TwoSum, bringing close to target
            else:
                return [l+1,r+1]
            
