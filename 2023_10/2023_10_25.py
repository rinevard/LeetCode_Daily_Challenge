# 2023/10/25 Daily challenge
# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 数学题
        def helper(n, k):
            if k == 1:
                return 0
            else:
                return helper(n - 1, k) if k <= pow(2, n - 2) else (1 + helper(n - 1, k - pow(2, n - 2))) % 2

        return helper(n, k)