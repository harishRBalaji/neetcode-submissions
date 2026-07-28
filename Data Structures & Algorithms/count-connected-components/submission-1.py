class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)

        if parent_of_u == parent_of_v:
            return False
        
        if self.size[parent_of_u] < self.size[parent_of_v]:
            parent_of_u, parent_of_v = parent_of_v, parent_of_u
        self.parent[parent_of_v] = parent_of_u
        self.size[parent_of_u] += self.size[parent_of_v]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        result = n
        for u, v in edges:
            if dsu.union(u, v):
                result -= 1
        return result