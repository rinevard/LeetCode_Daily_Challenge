# 2023/11/28 Daily challenge
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # 保证 corridor 以 'S' 开头，以 'S' 结尾，且非空
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                break
        for j in range(len(corridor) - 1, -1, -1):
            if corridor[j] == 'S':
                break
        corridor = corridor[i:j + 1]
        if corridor == "P": 
            corridor = ""
        if corridor == "":
            return 0

        # 把两组两个椅子组成的椅子对之间的植物聚集到一起
        # 此时 corridor 非空，且以 S 开头， S 结尾
        # 样例：'SPPSPSS' -> plants_cluster = [0, 1, 0]            
        plants_cluster = []
        chair_count = 0
        plant_count = 0

        for item in corridor:
            if item == 'S':
                chair_count += 1
                if chair_count == 2:
                    plants_cluster.append(plant_count)
                    plant_count = 0
                    chair_count = 0
            elif item == 'P':
                if chair_count == 0:
                    plant_count += 1
        plants_cluster.append(0)

        # 每个植物聚类中要放一个隔板，以此计算结果
        if chair_count == 1:
            return 0
        mod = pow(10, 9) + 7
        ans = 1
        for plant_num in plants_cluster:
            ans *= (1 + plant_num)

        return ans % mod