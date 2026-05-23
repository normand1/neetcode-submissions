from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        visited, cycle = set(), set()
        path = []

        for prereq in prerequisites:
            crs, pre = prereq
            adj_list[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in adj_list[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            path.append(crs)
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return path