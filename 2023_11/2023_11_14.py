# 2023/11/14 Daily challenge
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 存储每个字母的第一个和最后一个下标
        first_idx = {}
        last_idx = {}
        for i, char in enumerate(s):
            if char not in first_idx:
                first_idx[char] = i
            last_idx[char] = i

        ans = 0
        # 遍历每个字符，寻找位于它的首次和最后一次出现之间的不同字符
        for char in first_idx:
            unique_chars_between = set(s[first_idx[char]+1 : last_idx[char]])
            ans += len(unique_chars_between)

        return ans