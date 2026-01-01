class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 > 9:
                # Carry so keep going
                digits[i] = 0
                i -= 1
            else:
                # Just increment and return
                digits[i] += 1
                return digits
        # At this point, we need to append a 1 to the start of array
        new_digits = [1]
        new_digits.extend(digits)
        return new_digits