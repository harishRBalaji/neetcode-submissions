class DSU:
    def __init__(self, n):
        self.comps = n
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)

        if parent_of_u == parent_of_v:
            return False
        
        self.comps -= 1
        if self.size[parent_of_u] < self.size[parent_of_v]:
            parent_of_u, parent_of_v = parent_of_v, parent_of_u
        self.size[parent_of_u] += self.size[parent_of_v]
        self.parent[parent_of_v] = parent_of_u
        return True
    
    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1