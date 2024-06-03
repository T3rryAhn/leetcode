class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, row, col):
            # Check column
            for i in range(row):
                if board[i][col] == 1:
                    return False
            
            # Check left diagonal (top left to bottom right)
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1
            
            # Check right diagonal (top right to bottom left)
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1
            
            return True

        def place_queens(board, row):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 1
                    count += place_queens(board, row + 1)
                    board[row][col] = 0  # Backtrack
            return count
        
        board = [[0] * n for _ in range(n)]
        return place_queens(board, 0)