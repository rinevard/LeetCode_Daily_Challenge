# 2023/11/8 Daily challenge
# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1

        fx, fy = abs(fx - sx), abs(fy - sy)
        min_time = min(fx, fy) + abs(fx - fy)
        
        if t < min_time:
            return False

        return True