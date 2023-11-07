# 2023/11/7 Daily challenge
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

from math import ceil
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # 计算每个怪物还有多久到达面前即可
        time_to_die = [ceil(dist[i] / speed[i]) for i in range(len(dist))]
        time_to_die.sort()

        time, monster_ptr = 0, 0
        while monster_ptr < len(time_to_die) and time < time_to_die[monster_ptr]:
            monster_ptr += 1
            time += 1

        return monster_ptr