### 215 MEDIUM
### STATUS: SOLVED
### BEATS: 38%

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Negate values to use a max heap
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        # Pop the first k - 1 elements
        counter = 0
        while max_heap and counter < k - 1:
            heapq.heappop(max_heap)
            counter += 1
        # Return top value negated
        return -heapq.heappop(max_heap)
    
nums = [3, 2, 1, 5, 6, 5]
k = 2
a = Solution()
print(a.findKthLargest(nums, k))