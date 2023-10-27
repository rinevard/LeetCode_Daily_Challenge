# 2023/10/26 Daily challenge
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> int:
            # 以left和right为中心扩展，返回当前扩展的最大回文串的长度。
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1
        
        n = len(s)
        
        start, end = 0, 0
        for i in range(n):
            # 以i为中心的奇数长度回文串
            len1 = expandAroundCenter(i, i)
            # 以i和i+1为中心的偶数长度回文串
            len2 = expandAroundCenter(i, i + 1)
            max_len = max(len1, len2)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]


"""
# 这是一个更快的算法， 我会在语句旁给出注释
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        
        start, size = 0, 1
        # 在这里， 可以把i理解为字符串的终点， size为长度
        # 为什么这能保证我们找到最长回文字符串(设为s[st:ed])？
        # 这是因为， 由于最长回文串是最长的， 那么当i在某个
        # (st + ed) // 2之后的位置， 会有i - size > 0.
        # 而当i不断往后移动， size也不断更新， 直到我们走完这个最长回文字符串.
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            
            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                
        return s[start:start+size]
"""
