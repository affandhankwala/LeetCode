### 238: MEDIUM
### STATUS: SOLVED
### BEATS: 90%

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Get total product and count number of 0s
        total_prod = 1
        zeros = 0
        # Track product if we ignore 0s
        ignore_zero_product = 1
        for n in nums:
            total_prod *= n
            if n != 0:
                ignore_zero_product *= n
            else: 
                zeros += 1

        # Product of array except self
        new_arr = []
        for n in nums:
            try:
                val = total_prod / n
            except ZeroDivisionError:
                # If exactly 1 zero, we use ignore_zero_product
                if zeros == 1: val = ignore_zero_product
                # If more then we just set to 0
                else: val = 0
            new_arr.append(val)
        return new_arr
        
    

arr = [-1,1,0,-3,3]
a = Solution()
print(a.productExceptSelf(arr))