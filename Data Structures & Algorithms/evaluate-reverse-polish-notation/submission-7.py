class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = []
        result = 0
        for s in tokens:
            if s in ['+', '-', '*', '/']:
                
                r = operands.pop()
                l = operands.pop()

                operator = s
                if operator == "+":
                    result = l + r
                elif operator == "-":
                    result = l - r
                elif operator == "*":
                    result = l * r
                elif operator == "/":
                    result = int(l / r)

                operands.append(result)
            else:
                operands.append(int(s))
        return operands[0]
