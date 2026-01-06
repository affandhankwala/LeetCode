### 3459. HARD
### STATUS: UNSOLVED


class Solution(object):
    def search_diag_neighbors(self, grid, point, num):
        neighbors = []
        directions = []
        x, y = point
        # Top left
        if x - 1 >= 0 and y - 1 >= 0 and grid[x-1][y-1] == num:
            neighbors.append((x-1, y-1))
            directions.append("top_left")
        # Top right
        if x - 1 >= 0 and y + 1 < len(grid[0]) and grid[x-1][y+1] == num:
            neighbors.append((x-1, y+1))
            directions.append("top_right")
        # Bottom left
        if x + 1 < len(grid) and y - 1 >= 0 and grid[x+1][y-1] == num:
            neighbors.append((x+1, y-1))
            directions.append("bottom_left")
        # Bottom right
        if x + 1 < len(grid) and y + 1 < len(grid[0]) and grid[x+1][y+1] == num:
            neighbors.append((x+1, y+1))
            directions.append("bottom_right")
        return neighbors, directions

    def is_valid_direction(self, direction, next_direction):
        # Determine if the next direction is acceptable
        if direction == "top_left":
            if next_direction == "top_right": return True
            return False
        elif direction == "top_right":
            if next_direction == "bottom_right": return True
            return False
        elif direction == "bottom_right":
            if next_direction == "bottom_left": return True
            return False
        elif direction == "bottom_left":
            if next_direction == "top_left": return True
            return False
    
    def terminate(self, max_length, directions_list, adder=0):
        # Assess max_length
        max_length = max(max_length, len(directions_list) + adder)
        directions_list.pop()
        return max_length
    
    def remove_visited_neighbors(self, visited, neighbors, neighbor_dir): 
        i = 0
        while i < len(neighbors):
            if len(neighbors) <= 0: return
            if neighbors[i] in visited:
                neighbors.pop(i)
                neighbor_dir.pop(i)
                i -= 1
            else:
                i += 1

    def get_next_val(self, current_val):
        if current_val == 0: return 2
        return 0

    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Iterate through the entire grid looking for 1
        # Once a 1 is found, search diagonal neighbors for a 2. 
        # Explore each 2. Explore by searching diagonal neighbors for a 0
        # If 0 found in same direction as previous, we again search for a 2
        # Once we turn clockwise, we only search in the new direction.
        # Store the max result and recurse backwards
        max_length = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    # Start V
                    # Set max_length to 1 as well
                    max_length = max(max_length, 1)
                    neighbors, directions = self.search_diag_neighbors(grid, (x, y), 2)
                    for i in range(len(neighbors)):
                        switched_direction = False
                        starting_neighbor = neighbors[i]
                        starting_direction = directions[i]
                        directions_list = []
                        # Start 0, 2 search
                        neighbor_stack = [starting_neighbor]
                        direction_stack = [starting_direction]
                        visited = []
                        while len(neighbor_stack) > 0:
                            cur = neighbor_stack.pop()
                            cur_dir = direction_stack.pop()
                            # Check if we have already visited
                            if cur in visited:
                                continue
                            visited.append(cur)
                            next_val = self.get_next_val(grid[cur[0]][cur[1]])
                            directions_list.append(cur_dir)
                            # Check if we switched directions
                            if len(directions_list) > 1:
                                # Not First move
                                previous_direction = directions_list[len(directions_list) - 2]
                                if previous_direction != cur_dir:
                                    # Toggle switch if not toggled and valid direction
                                    if not switched_direction: 
                                        if self.is_valid_direction(previous_direction, cur_dir):
                                            switched_direction = True
                                        # Terminate if invalid direction
                                        else: 
                                            max_length = self.terminate(max_length, directions_list)
                                            continue
                                    # If switch direction is already toggled, terminate
                                    else:
                                        max_length = self.terminate(max_length, directions_list)
                                        continue
                            cur_neighbors, cur_neighbor_directions = self.search_diag_neighbors(grid, cur, next_val)
                            self.remove_visited_neighbors(visited, cur_neighbors, cur_neighbor_directions)
                            # If no neighbors, count length of V
                            if len(cur_neighbors) <= 0: 
                                max_length = self.terminate(max_length, directions_list, adder = 1) 
                                continue
                            # If we have neighbors, add them to the stacks
                            for j in range(len(cur_neighbors)):
                                neighbor_stack.append(cur_neighbors[j])
                                direction_stack.append(cur_neighbor_directions[j])
                # If grid position is not 1, move along
        return max_length

# TODO: length is a bit funky. previous direction needs to revert if back tracking
 
cases = [
    # [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]],
    # [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]],
    # [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]],
    # [[1]],
    # [[0,2,0,2,0,2,0],[0,2,0,2,1,2,0],[0,2,0,2,0,2,0]],
    [[0,0,2,0,0,1,1,2,0,0,0,0,0,0,2,0],[2,2,2,1,0,2,2,2,0,2,2,2,2,0,2,2],[0,1,0,0,2,0,2,0,0,0,0,1,0,0,0,1]],

]
a = Solution()
for case in cases:
    max_length = a.lenOfVDiagonal(case)
    print(max_length)