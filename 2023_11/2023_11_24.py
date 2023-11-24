# 2023/11/24 Daily challenge
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 我们只要最小化 Bob 和 Alice 的收益即可
        # 让 Bob 拿最小的 n 组硬币，让 YOU 和 Alice依次拿剩下的
        sorted_piles = sorted(piles)
        st = len(sorted_piles) // 3
        ans = 0

        for i in range(st, len(sorted_piles)):
            if (st - i) % 2 == 0:
                ans += sorted_piles[i]
        return ans