class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # #Brute Force; Time Complexity O(n2)
        # res = 0
        
        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         area = (r - l) * min(heights[l], heights[r])
        #         res = max(area, res)

        # return res

        # Linear Programming: Two Pointers; Time Complexity O(n)
        res = 0

        #initializing pointers
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)

            #Increment left pointer if l<r, decrement right pointer if r<l, change l or r pointer if l=r
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res


        