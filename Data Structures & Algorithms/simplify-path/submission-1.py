class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for dir in paths:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir != "" and dir != ".":
                stack.append(dir)
        
        return "/" + "/".join(stack)