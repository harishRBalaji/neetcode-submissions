class Solution:

    '''
    U:
        I - unix path: string
        O - canonical path: string
        C - given
        E - root directory, empty directory, etc.
    Plan:
        1. Initialize a stack
        2. for i in range(len(path)):
            2.1 if stack[-1] == '/' and path[i] == '/'
                ignore
            2.2 else if stack
    '''
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