class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = 0
                match token:
                    case "+":
                        result = operand_1 + operand_2
                    case "-":
                        result = operand_1 - operand_2
                    case "*":
                        result = operand_1 * operand_2
                    case "/":
                        result = int(operand_1 / operand_2)
                stack.append(result)
        return stack[-1]