from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def count_islands(start_r, start_c):
            if (start_r, start_c) in visited or grid[start_r][start_c] == "0":
                return 0
            queue = deque()
            queue.append((start_r,start_c))
            visited.add((start_r,start_c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue:
                r, c = queue.popleft()
                for dr in dirs:
                    dr_r, dr_c = dr
                    new_r, new_c = r + dr_r, c + dr_c

                    if (new_r not in range(rows) or 
                    new_c not in range(cols) or 
                    grid[new_r][new_c] == "0" or 
                    (new_r,new_c) in visited):
                        continue
                    else:
                        visited.add((new_r,new_c))
                        queue.append((new_r,new_c))
            
            return 1

        for r in range(rows):
            for c in range(cols):
                count += count_islands(r, c)

        return count

            
