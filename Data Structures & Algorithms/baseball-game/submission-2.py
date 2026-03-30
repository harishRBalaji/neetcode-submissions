class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_score = 0
        for ops in operations:
            if ops == "+":
                new_element = stack[-1] + stack[-2]
                stack.append(new_element)
                total_score += new_element
            elif ops == "D":
                new_element = 2 * stack[-1]
                stack.append(new_element)
                total_score += new_element
            elif ops == "C":
                removed_element = stack.pop()
                total_score -= removed_element
            else:
                new_element = int(ops)
                stack.append(new_element)
                total_score += new_element

        return total_score