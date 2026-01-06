class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # Find the number of negative numbers and zeros. If odd number, return sum of entire matrix minus largest_negative. Else return sum of entire matrix
        sum_of_matrix, negative_nums, smallest_abs = 0, 0, 999999
        for row in matrix:
            for element in row: 
                if abs(element) < smallest_abs: 
                    smallest_abs = abs(element)
                sum_of_matrix += abs(element)
                if element <= 0: 
                    negative_nums += 1
        if negative_nums % 2 == 1: 
            return sum_of_matrix - (2 * smallest_abs)
        return sum_of_matrix

        