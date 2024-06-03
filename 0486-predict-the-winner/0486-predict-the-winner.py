class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        if n % 2 == 0:
            return True

        dp = [[0] * n for _ in range(n)]

        # 대각선 채우기
        for i in range(n):
            dp[i][i] = nums[i]

        # dp 피라미드 차곡차곡 쌓아 올리기
        for i in range(1, n):
            for j in range(n - i):
                dp[j][i+j] = max(nums[j] - dp[j+1][i+j], nums[i+j] - dp[j][i+j-1])

        return dp[0][n - 1] >= 0