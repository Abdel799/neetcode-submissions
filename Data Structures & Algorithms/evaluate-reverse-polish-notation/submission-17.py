class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            if token != "+" and token != "*" and token != "-" and token != "/":
                stack.append(int(token))
            
            elif token == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            
            elif token == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            
            elif token == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(a*b))
            
            elif token == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))

        return stack[-1]
