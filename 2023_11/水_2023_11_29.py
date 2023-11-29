# 2023/11/29 Daily challenge
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n % 2
            n //= 2
        return ans