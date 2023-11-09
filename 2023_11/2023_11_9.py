# 2023/11/9 Daily challenge
# https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = pow(10, 9) + 7
        # 对每个形如 'aaaaxxx' 的字符串，把它分为 'aaaa' 和 'xxx'
        # 'aaaa'包含四个 'a'，三个 'aa'，两个 'aaa'，一个 'aaaa'
        homogenous_len = lambda sub_len: ((sub_len + 1) * sub_len) // 2
        ans = 0
        same_len = 1
        
        # 把原字符串分成若干部分，使每部分的substring的所有字符相同
        # 且每两个相邻的部分的字符不同。
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                same_len += 1
            else:
                ans += homogenous_len(same_len)
                same_len = 1

        ans += homogenous_len(same_len)
        return ans % mod