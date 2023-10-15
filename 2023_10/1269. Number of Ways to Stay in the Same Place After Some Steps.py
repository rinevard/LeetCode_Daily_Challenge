# 2023/10/15 Daily challenge
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        modulo = pow(10, 9) + 7
        maxLen = min(arrLen, steps // 2 + 1)

        # dp[i][j]表示消耗i步到j处的步数，且指针从未移出arrLen//2之外（因为最终目的是返回原点）
        dp = [[0 for _ in range(maxLen)] for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(maxLen):
                if j - 1 >= 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % modulo
                if j + 1 < maxLen:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % modulo
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % modulo
                
        return dp[steps][0]