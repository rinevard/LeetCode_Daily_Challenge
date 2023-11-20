# 2023/11/20 Daily challenge
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # 初始化垃圾计数和每种垃圾最后出现的位置
        garbage_count = {'M': 0, 'P': 0, 'G': 0}
        last_garbage_house = {'M': 0, 'P': 0, 'G': 0}
        time_to_travel = [0]

        # 遍历每个房子，同时更新垃圾计数和最后垃圾位置
        for i, garbs in enumerate(garbage):
            for garb in garbs:
                garbage_count[garb] += 1
                last_garbage_house[garb] = i
            if i < len(travel):
                time_to_travel.append(time_to_travel[i] + travel[i])

        # 计算拾取垃圾所需的时间和驾驶时间
        time_to_pick = sum(garbage_count.values())
        time_to_drive = sum(time_to_travel[last_garbage_house[garb]] for garb in last_garbage_house)

        return time_to_pick + time_to_drive
