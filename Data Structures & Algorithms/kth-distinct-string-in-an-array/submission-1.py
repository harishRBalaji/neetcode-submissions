class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = set()
        visited = set()

        for s in arr:
            if s in distinct:
                distinct.remove(s)
                visited.add(s)
            elif s not in visited:
                distinct.add(s)
        
        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s
        return ""