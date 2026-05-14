class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Prefix Postfix (Optimal)
        res = [1] * (len(nums))  #initializing op array to 1

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #Assign prefix to res[i]
            prefix *= nums[i] #updating prefix by multiplying with nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):  
            #range(start, stop, step) i.e. start at last index, stop at 0th and step -1 means go reverse
            res[i] *= postfix  #res[i] is product of prefix and postfix
            postfix *= nums[i]

        return res