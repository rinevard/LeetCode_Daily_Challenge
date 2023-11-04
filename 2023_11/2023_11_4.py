# 2023/11/4 Daily challenge
# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max([i for i in left]+[n - j for j in right])