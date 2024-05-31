class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def check_col(col_idx):
            count = 0
            for i in range(len(grid)):
                if grid[i][col_idx]:
                    count += 1
            if count > 1:
                return True
            return False
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if sum(grid[i]) > 1 or check_col(j):
                        answer += 1
        return answer
