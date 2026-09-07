class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return 0
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return 1

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        for r in range(ROWS):
            prev = -1
            for c in range(COLS):
                if grid[r][c] == 1:
                    if prev != -1:
                        dsu.union(prev, r * COLS + c)
                    prev = r * COLS + c

        for c in range(COLS):
            prev = -1
            for r in range(ROWS):
                if grid[r][c] == 1:
                    if prev != -1:
                        dsu.union(prev, r * COLS + c)
                    prev = r * COLS + c

        # Count servers in components of size > 1
        from collections import defaultdict
        comp_size = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    comp_size[dsu.find(r * COLS + c)] += 1

        return sum(size for size in comp_size.values() if size > 1)