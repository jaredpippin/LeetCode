class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(i, j, visited):
            if (i, j) in visited or i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return 0
            else:
                visited.add((i, j))
                dfs(i + 1, j, visited)
                dfs(i - 1, j, visited)
                dfs(i, j + 1, visited)
                dfs(i, j - 1, visited)
                return 1
            
        count = 0
        for i in range(rows):
            for j in range(cols):
                count += dfs(i, j, visited)
        return count