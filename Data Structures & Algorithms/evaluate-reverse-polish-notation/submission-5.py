class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        handleOperation = {'+', '-', '*', '/'}
        for i in tokens:
            if i not in handleOperation:
                stack.append(int(i))
            else:
                firstNumber = stack.pop()
                secondNumber = stack.pop()
                if i == '+':
                    stack.append(firstNumber+secondNumber)
                elif i == '-':
                    stack.append(secondNumber-firstNumber)
                elif i == '*':
                    stack.append(firstNumber*secondNumber)
                elif i == '/':
                    stack.append(int(float(secondNumber)/firstNumber))
        if stack:
            return int(stack[-1])
        else:
            return None