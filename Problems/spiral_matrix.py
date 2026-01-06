### 54 MEDIUM
### STATUS: SOLVED
### BEATS: 100%
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top_off, right_off, bot_off, left_off = 0, 0, 0, 0
        # Spiral by hitting walls top, right, bot, left
        walls = ["top", "right", "bot", "left"]
        wall_ind = 0
        row, col = 0, 0
        spiral = []
        # Loop until opposite offsets touch
        while (top_off + bot_off < len(matrix)) and (right_off + left_off < len(matrix[0])):
            chosen_wall = walls[wall_ind]
            if chosen_wall == "top":
                # Top wall (account for right offset)
                while col < len(matrix[row]) - right_off:
                    spiral.append(matrix[row][col])
                    col += 1
                top_off += 1
                # Reset col
                col -= 1
                row += 1
            elif chosen_wall == "right":
                # Right wall (account for bottom offset)
                while row < len(matrix) - bot_off:
                    spiral.append(matrix[row][col])
                    row += 1
                right_off += 1
                # Reset row
                col -= 1
                row -= 1
            elif chosen_wall == "bot":
                # Bot wall (account for left offset)
                while col > -1 + left_off:
                    spiral.append(matrix[row][col])
                    col -= 1
                bot_off += 1
                # Reset col
                col += 1
                row -= 1
            elif chosen_wall == "left":
                # Left wall (account for top offset)
                while row > -1 + top_off:
                    spiral.append(matrix[row][col])
                    row -= 1
                left_off += 1
                # Reset row 
                col += 1
                row += 1
            wall_ind += 1
            wall_ind %= len(walls)
        return spiral
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a = Solution()
print(a.spiralOrder(matrix))