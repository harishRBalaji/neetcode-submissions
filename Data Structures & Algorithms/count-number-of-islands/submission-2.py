class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        root_of_x = self.find(x)
        root_of_y = self.find(y)

        if root_of_x == root_of_y:
            return False
        if self.rank[root_of_x] >= self.rank[root_of_y]:
            self.parent[root_of_y] = root_of_x
            self.rank[root_of_x] += self.rank[root_of_y]
        else:
            self.parent[root_of_x] = root_of_y
            self.rank[root_of_y] += self.rank[root_of_x]
        return True

class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0'):
                            continue
                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1
        return islands