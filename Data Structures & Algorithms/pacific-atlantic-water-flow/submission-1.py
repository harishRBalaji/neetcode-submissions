class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs solution
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific, atlantic = set(), set()

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        pacific_border_cells = []
        atlantic_border_cells = []

        for c in range(COLS):
            pacific_border_cells.append((0, c))
            atlantic_border_cells.append((ROWS - 1, c))
        
        for r in range(ROWS):
            pacific_border_cells.append((r, 0))
            atlantic_border_cells.append((r, COLS - 1))
        
        bfs(pacific_border_cells, pacific)
        bfs(atlantic_border_cells, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res