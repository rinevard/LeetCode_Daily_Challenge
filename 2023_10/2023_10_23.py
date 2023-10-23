# 2023/10/23 Daily challenge
# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False

        # (n & n - 1) == 0 判断一个数是否是2的幂次，
        # (2^(2k+1) - 1) % 3 == 1, (2^(2k) - 1) % 3 == (4^k - 1) % 3 == 0
        return (n & n - 1) == 0 and (n - 1) % 3 == 0