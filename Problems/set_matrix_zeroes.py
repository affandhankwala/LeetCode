### 73. MEDIUM
### STATUS: SOLVED
### BEATS: 73%
class Solution(object):
    def alterMatrix(self, matrix, zero_location):
        row, col = zero_location
        # Change all elements in row to 0
        for i in range(len(matrix[row])):
            matrix[row][i] = 0
        # Change all elements in col to 0
        for i in range(len(matrix)):
            matrix[i][col] = 0

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Store locations of 0's in matrix
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        # For each zero, alter the matrix
        for zero_location in zeros:
            self.alterMatrix(matrix, zero_location)
        # Return altered matrix
        return matrix
