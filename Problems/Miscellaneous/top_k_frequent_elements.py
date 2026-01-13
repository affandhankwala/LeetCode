### 347 MEDIUM
### STATUS: SOLVED
### BEATS: 85%
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0: 
            return nums
        # Define dictionary
        frequency = {}
        for i in nums: 
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        top_k = [e for e, f in heapq.nlargest(k, frequency.items(), key=lambda x: x[1])]

        return top_k    