class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Binary search  with Time complexity O(log n) always used in Rotated Sorted Array
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            #If target is mid, return mid
            if nums[mid] == target:
                return mid
            
            #Check if left sorted array, search right else search left
            # If in left sorted array, check if target > mid or target < l, search right
            # If in right sorted array, check if target < mid or target > r, search left
            if nums[l] <= nums[mid]: #Left sorted array
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: #Right sorted array
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1