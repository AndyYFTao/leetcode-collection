# https://leetcode.com/problems/maximal-square/discuss/524509/Python-Dynamic-Programming-Video-Explanation

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        dp, M = [[0 for col in range(len(matrix[0]) + 1)] for row in range(len(matrix) + 1)], 0

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == "1":
                    l = [dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]]
                    dp[i][j] = min(l) + 1
                M = max(M, dp[i][j])

        return M * M