
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        largest_diagonal = -1
        largest_area = -1
        for rect in dimensions:
            length, width = rect[0], rect[1]
            diagonal = (length ** 2 + width ** 2) ** (1/2)
            area = length * width
            print("L: ",length, " W: ", width, " D: ", diagonal, " A: ", area)
            if diagonal > largest_diagonal:
                largest_diagonal = diagonal
                largest_area = area
            elif diagonal == largest_diagonal:
                if area > largest_area:
                    largest_area = area
                    largest_diagonal = diagonal
        return largest_area
                

arr = [[2,6],[5,1],[3,10],[8,4]]
a = Solution()
print(a.areaOfMaxDiagonal(arr))