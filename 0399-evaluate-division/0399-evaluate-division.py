class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 변수와 인덱스 딕셔너리로 저장하기
        vars = {}
        idx = 0
        for e in equations:
            for v in e:
                if v not in vars:
                    vars[v] = idx
                    idx += 1

        # 그리드 초기화
        grid = [[-1.0] * len(vars) for _ in range(len(vars))]

        for i in range(len(values)):
            row = vars[equations[i][0]]
            col = vars[equations[i][1]]
            grid[row][col] = values[i]
            grid[col][row] = 1 / values[i]

        # 대각 선 '1.0` 으로 초기화
        for i in range(len(vars)):
            grid[i][i] = 1.0

        # 피라미드 채우기
        for k in range(len(grid)): 
            for j in range(len(grid)):
                for i in range(len(grid)):
                    if grid[i][k] != -1.0 and grid[k][j] != -1.0:
                        if grid[i][j] == -1.0 or grid[i][j] > grid[i][k] * grid[k][j]:
                            grid[i][j] = grid[i][k] * grid[k][j]


        answer = []
        for q in queries:
            if q[0] in vars and q[1] in vars:
                row = vars[q[0]]  # 행이 분자
                col = vars[q[1]]  # 열이 분모

                if (0.99990 < grid[row][col] < 1.0):
                    answer.append(1.0)
                else:
                    answer.append(grid[row][col])
            else:
                answer.append(-1.0)

        return answer
