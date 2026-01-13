### 118. EASY
### STATUS: SOLVED
### BEATS: 100%

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return self.recursivePascal(numRows)
        

    def recursivePascal(self, numRows):
        if numRows < 1: 
            return [[]]
        if numRows == 1:
            return [[1]]

        output = self.recursivePascal(numRows - 1)
        prev_row = output[len(output) - 1]
        # Calculate new row 
        new_row = [1]
        i, j = 0, 1
        while j < len(output):
            new_row.append(prev_row[i] + prev_row[j])
            i += 1
            j += 1
        # Add final 1
        new_row.append(1)
        output.append(new_row)
        # Return output
        return output

numRows = 5
a = Solution()
print(a.generate(numRows))
