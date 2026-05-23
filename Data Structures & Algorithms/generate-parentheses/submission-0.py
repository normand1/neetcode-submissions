class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        curr = []

        def combinations(openN, closeN):
            if openN == n and closeN == n:
                res = "".join(curr)
                result.append(res)
                return
            
            if openN < n:
                curr.append("(")
                combinations(openN + 1, closeN)
                curr.pop()
            if closeN < openN and closeN < n:
                curr.append(")")
                combinations(openN, closeN + 1)
                curr.pop()
                
        combinations(0,0)
        return result
                        

