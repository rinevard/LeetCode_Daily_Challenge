# 2023/10/19 Daily challenge
# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i_back, j_back = 0, 0
            
            while i >= 0:
                if s[i] == '#':
                    i_back += 1
                    i -= 1
                elif i_back > 0:
                    i_back -= 1
                    i -= 1
                else:
                    break  # Break when a character to compare is found or i is out of range
            
            while j >= 0:
                if t[j] == '#':
                    j_back += 1
                    j -= 1
                elif j_back > 0:
                    j_back -= 1
                    j -= 1
                else:
                    break  # Break when a character to compare is found or j is out of range
            
            # If either i or j is out of range, one string is longer than the other
            if (i >= 0) != (j >= 0):
                return False
            
            # If characters at i and j are different, return False
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            # Move to the next position for comparison
            i -= 1
            j -= 1

        return True