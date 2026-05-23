class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = 0
        memo = {}
        def backtrack(curr, memo):
            nonlocal res
            if curr > n:
                return
            if curr == n:
                res += 1
                return

            backtrack(curr + 1, memo)
            backtrack(curr + 2, memo)
        
        backtrack(0, memo)
        return res
