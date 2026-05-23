class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, subarray, total):
            print(subarray)
            if total == target:
                res.append(subarray.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            subarray.append(candidates[i])
            dfs(i + 1, subarray, total + candidates[i])
            subarray.pop()
            while (i + 1 < len(candidates) and
             candidates[i] == candidates[i + 1]):
                i += 1
            dfs(i + 1, subarray, total)

        dfs(0, [], 0)
        return res