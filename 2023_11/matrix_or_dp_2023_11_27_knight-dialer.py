# 2023/11/27 Daily challenge
# https://leetcode.com/problems/knight-dialer/

import numpy as np

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        mod = 10**9 + 7
        # 转移矩阵
        # 把数字分为五类(4, 6)，(1, 3, 7, 9)，(0)，(2, 8)，(5)，其中5不参与计算。
        transition_matrix = np.array([[0, 1, 2, 0], [2, 0, 0, 2], [1, 0, 0, 0], [0, 1, 0, 0]])
        # 对矩阵的每个元素取模，以防止溢出
        transition_matrix = np.mod(transition_matrix, mod)

        # 矩阵快速幂
        def matrix_power(matrix, power):
            result = np.eye(matrix.shape[0], dtype=np.int64)
            while power > 0:
                if power % 2:
                    result = np.mod(np.matmul(result, matrix), mod)
                matrix = np.mod(np.matmul(matrix, matrix), mod)
                power //= 2
            return result

        power = matrix_power(transition_matrix, n - 1)

        # 初始矩阵
        st_matrix = np.array([1, 1, 1, 1])
        tmp = np.mod(np.matmul(st_matrix, power), mod)

        # 应用系数矩阵
        coeff_matrix = np.array([2, 4, 1, 2])
        ans = np.mod(np.matmul(tmp, coeff_matrix), mod)

        return ans
        

"""
MOD = 10**9 + 7
moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

dp = [1 for _ in range(10)]

for m in range(2, n+1):
    new_dp = []
    for currDigit in range(10): 
        # sum这一步应该耗费了较多时间
        new_dp.append(sum([dp[nextDigit] for nextDigit in moves[currDigit]]) % MOD)
    dp = new_dp
return sum([dp[i] for i in range(10)]) % MOD
"""