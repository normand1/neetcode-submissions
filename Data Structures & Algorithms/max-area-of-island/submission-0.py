from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        max_island_size = 0

        def find_island_size(r, c):
            nonlocal max_island_size
            if (grid[r][c] == 0 
            or (r,c) in visited):
                return

            max_size = 1
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue:
                temp_r, temp_c = queue.popleft()
                for dr in dirs:
                    new_r, new_c = dr[0] + temp_r, dr[1] + temp_c

                    if (new_r not in range(rows) 
                    or new_c not in range(cols) 
                    or grid[new_r][new_c] == 0
                    or (new_r, new_c) in visited):
                        visited.add((new_r,new_c))
                        continue
                    
                    else:
                        max_size += 1
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                    
            max_island_size = max(max_island_size, max_size)

        for r in range(rows):
            for c in range(cols):
                find_island_size(r, c)
        
        return max_island_size