class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        second_vs_first_parantheses = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for c in s:
            if c in second_vs_first_parantheses:
                if stack and stack[-1] == second_vs_first_parantheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
