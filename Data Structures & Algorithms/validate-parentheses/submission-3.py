class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {'(': ')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            if c in brackets.values():
                if len(stack) > 0:
                    curr = stack.pop()
                    if brackets[curr] == c:
                        continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
