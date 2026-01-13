### 152. MEDIUM
### STATUS: SOLVED
### BEATS: 22%

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1: return 0
        min_prod, max_prod, result_prod = nums[0], nums[0], nums[0]

        for n in nums[1:]:
            # Get three points
            p_n = n
            p_min = min_prod * n
            p_max = max_prod * n
            # Reassign min, and max prod
            min_prod = min(p_n, p_min, p_max)
            max_prod = max(p_n, p_min, p_max)
            # Reassign result
            result_prod = max(result_prod, min_prod, max_prod)
        return result_prod
        

arr = [2,3,-2,4]
a = Solution()
print(a.maxProduct(arr))