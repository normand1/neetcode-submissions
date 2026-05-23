from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)

        for prereqs in prerequisites:
            crs, pre = prereqs
            adj_list[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            elif len(adj_list[crs]) == 0:
                return True
            
            visited.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            return True

        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True