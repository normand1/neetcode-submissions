class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
      
        res = []        
        def dfs(i, subarray, total):

            if total == target:
                res.append(subarray)
                return
            if i >= len(nums) or total > target:
                return

            

            dfs(i, subarray + [nums[i]], total + nums[i])
            dfs(i + 1, subarray, total)
        
        dfs(0, [], 0)
        return res


