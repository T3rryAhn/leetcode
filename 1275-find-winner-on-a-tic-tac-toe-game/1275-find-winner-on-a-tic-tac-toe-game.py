class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[''] * 3 for _ in range(3)]

        # fill board
        for i in range(len(moves)):
            if i % 2:
                board[moves[i][0]][moves[i][1]] = 'O'
            else:
                board[moves[i][0]][moves[i][1]] = 'X'
        # check row
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    return 'A'
                elif board[i][0] == 'O':
                    return 'B'

        # check col
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    return 'A'
                elif board[0][i] == 'O':
                    return 'B'

        # check cross
        if board[1][1] == board[0][0] == board[2][2]:
            if board[1][1] == 'X':
                return 'A'
            elif board[1][1] == 'O':
                return 'B'
        elif board[1][1] == board[2][0] == board[0][2]:
            if board[1][1] == 'X':
                return 'A'
            elif board[1][1] == 'O':
                return 'B'

        # Nothing checked
        if len(moves) == 9:
            return "Draw"
        return "Pending"