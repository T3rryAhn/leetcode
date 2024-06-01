class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def in_range(y, x):
            return 0 <= y < len(grid) and 0 <= x < len(grid[0])
        
        dx = (1, 0, -1, 0)
        dy = (0, -1, 0, 1)
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0

        def dfs(y, x):
            visited[y][x] = True

            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if in_range(n_y, n_x) and not visited[n_y][n_x] and grid[n_y][n_x] == "1":
                    dfs(n_y, n_x)

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1" and not visited[m][n]:
                    count += 1
                    dfs(m, n)

        return count
        



    