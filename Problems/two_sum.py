### 1. EASY
### STATUS: SOLVED

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        # Make a dictionary of elements
        for i, n in enumerate(nums):
            # Store num as key and index as value
            d[n] = i

        # Look through list and find first pair
        for i, n in enumerate(nums):
            other_num = target - n
            if other_num in d:
                if d[other_num] != i:
                    return [i, d[other_num]]
        return []