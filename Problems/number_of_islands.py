### 200. MEDIUM
### STATUS: SOLVED
### BEATS: 28.5%
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_count = 0
        if not grid:
            return 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # See if is island
                if grid[y][x] != '0':
                    # Explore island and change set island to 0
                    grid = self.exploreIsland(grid, [y, x])
                    island_count += 1
                # Water and not visited
        return island_count
            
        
    def exploreIsland(self, grid, location):
        # See if location valid
        y, x = location
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            # Boundary
            return grid
        # See if location is water
        if grid[y][x] == '0':
            return grid
        # Else explore neighbors and mark current as 0
        grid[y][x] = '0'
        # Left
        grid = self.exploreIsland(grid, [y - 1, x])
        # Up
        grid = self.exploreIsland(grid, [y, x - 1])
        # Right
        grid = self.exploreIsland(grid, [y + 1, x])
        # Down
        grid = self.exploreIsland(grid, [y, x + 1])
        return grid

    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
a = Solution()
print(a.numIslands(grid))