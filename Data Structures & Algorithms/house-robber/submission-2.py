class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums) - 1
        if n == 0:
            return nums[0]
        elif n == 1:
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        
        def helper(n):
            
            if n in memo:
                return memo[n]
            
            memo[n] = max(nums[n] + helper(n - 2), helper(n - 1))
            return memo[n]
        
        return helper(n)

