class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            elif token == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            else:
                stack.append(int(token))
        return stack.pop()