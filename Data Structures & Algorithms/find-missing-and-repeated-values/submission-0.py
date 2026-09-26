class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        visited = set()
        repeated = missing = 0

        for i in range(N):
            for j in range(N):
                if grid[i][j] in visited:
                    repeated = grid[i][j]
                visited.add(grid[i][j])
        
        for num in range(1, N * N + 1):
            if num not in visited:
                missing = num
                break
        return [repeated, missing]