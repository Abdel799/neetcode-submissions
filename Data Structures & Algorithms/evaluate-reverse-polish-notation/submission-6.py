class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
    
        for op in tokens:

            if op != "+" and op != '-' and op != '*' and op != '/':
                stack.append(int(op))

            elif op == '+':

                result = stack.pop() + stack.pop()
                stack.append(result)
            
            elif op == '-':

                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)

            elif op == '*':

                result = stack.pop() * stack.pop()
                stack.append(result)

            elif op == '/':

                a = stack.pop()
                b = stack.pop()
                result = int(b / a)
                stack.append(result)
        
        return stack[-1]
        