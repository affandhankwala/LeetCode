### 153: MEDIUM
### STATUS: SOLVED
### BEATS: 100%


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findMinRecursive(nums, 0, len(nums) - 1)
    
    def findMinRecursive(self, nums, start, end):
        # Get mid
        mid = int((start + end) / 2)
        # Get nums
        start_num = nums[start]
        mid_num = nums[mid]
        end_num = nums[end]

        # If length <= 2, return min
        if end - start <= 1: 
            return min(start_num, end_num)
        
        # Determine which side it would be on
        if mid_num > end_num:
            # Search second half
            return self.findMinRecursive(nums, mid, end)
        if start_num > mid_num:
            # Search first half
            return self.findMinRecursive(nums, start, mid)
        # Has to to be in order
        return start_num

        
arr = [5,1,2,3,4]
a = Solution()
print(a.findMin(arr))