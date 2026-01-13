class Solution(object):

    def change_digit(self, string_num, old, new):
        new_string = ""
        for i in range(len(string_num)):
            if string_num[i] == old:
                new_string += str(new)
            else:
                new_string += string_num[i]
        return new_string

    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Max is most left digit that is not a 9
        string_num = str(num)
        max_digit = -1
        i = 0
        while max_digit == -1 and i < len(string_num):
            if string_num[i] != str(9):
                max_digit = string_num[i]
            else:
                i += 1
        max_new_num = 9
        min_new_num = 0
        # If number is all 9's largest number is 888...8
        if i == len(string_num):
            max_digit = 9
            max_new_num = 8
        min_digit = string_num[0]
        # Get max
        maximum = int(self.change_digit(string_num, max_digit, max_new_num))
        # Get min
        minimum = int(self.change_digit(string_num, min_digit, min_new_num))
        return maximum - minimum
    
i = 11891
a = Solution()
print(a.minMaxDifference(i))