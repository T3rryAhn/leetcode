class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = set()

        def dfs(left, right, s):
                if left == right == n:
                    answer.add(s)
                    return 

                if left < n:
                    dfs(left + 1, right, s + '(')
                if right < left:
                    dfs(left, right + 1, s + ')')
            
        dfs(0, 0, '')
        return list(answer)