### 2257 MED
### STATUS:
### BEATS:

class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # Create set with all walls
        wall_set = set()
        for w in walls: 
            wall_set.add(tuple(w))

        # Create set for all positions that are guarded
        guarded_positions = set()
        for guard in guards: 
            guard_position = tuple(guard)
            # Store guards position as tuple into guarded set
            guarded_positions.add(guard_position)

            # Determine furthest direction 
            # Max(top distance, right distance, bottom distance, left distance)
            furthest_direction = max(guard_position[0], n - guard_position[1], m - guard_position[0], guard_position[1])
            # Generate scanning locations. 
            scanning_locations = [[0 for _ in range(furthest_direction)] for _ in range(4)]
            for i in range(1, furthest_direction + 1):
                # Up scan
                scanning_locations[0][i - 1] = [guard_position[0] - i, guard_position[1]]
                # Right scan
                scanning_locations[1][i - 1] = [guard_position[0], guard_position[1] + i]
                # Down scan
                scanning_locations[2][i - 1] = [guard_position[0] + i, guard_position[1]]
                # Left scan 
                scanning_locations[3][i - 1] = [guard_position[0], guard_position[1] - i]

            # Add scanning locations to guarded position if they are not met with a wall 
            for d in range(len(scanning_locations)):
                for p in range(len(scanning_locations[d])):
                    # If meet wall, break 
                    position = tuple(scanning_locations[d][p])
                    # If invalid position, break
                    if position[0] < 0 or position[0] >= m or position[1] < 0 or position[1] >= n:
                        break
                    if position in wall_set: 
                        break
                    # Otherwise, add to guarded_set
                    else: 
                        guarded_positions.add(position)
            # Go to next guard
        unguarded_positions = (m * n) - len(guarded_positions) - len(wall_set)
        return unguarded_positions



guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
m, n = 4, 6
a= Solution()
print(a.countUnguarded(m, n, guards, walls))
