# 2023/10/31 Daily challenge
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        # xor(a, b) == c <=> xor(a, c) = b

        return [pref[i-1] ^ pref[i] if i != 0 else pref[i] for i in range(len(pref))]