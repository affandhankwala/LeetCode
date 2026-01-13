### 53. MED
### STATUS: SOLVED
### BEATS: 84%
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        cur_sum, max_sum = 0, nums[0]

        for n in nums:
            # Reset cur_sum is less than 0
            if cur_sum < 0:
                cur_sum = n
            # Else add current number to cur_sum
            else:
                cur_sum += n
            # Update max
            max_sum = max(cur_sum, max_sum)
        return max_sum