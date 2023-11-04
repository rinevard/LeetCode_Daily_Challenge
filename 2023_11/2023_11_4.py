# 2023/11/4 Daily challenge
# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

# 把相遇的蚂蚁互换编号，相当于两只蚂蚁穿过了对方。
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max([i for i in left]+[n - j for j in right])
