# 2023/10/14 Daily challenge
# 2742_Painting the Walls
# https://leetcode.com/problems/painting-the-walls/
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(time)
        can_print = [1 + free_print for free_print in time]

        # dp[i][j]表示从cost[i:]开始，还需要刷j个墙的最小cost
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # 从cost[n:]开始是空列表，如果还需要刷的墙不为0，那么不可能刷完，cost为无穷大
        for j in range(1, n+1):
            dp[n][j] = float('inf')

        for i in range(n-1, -1, -1):
            for j in range(1, n+1):
                # 可以选择在i处刷或不刷
                dp[i][j] = min(dp[i+1][j], cost[i] + dp[i+1][max(0, j - can_print[i])])

        return dp[0][n]
