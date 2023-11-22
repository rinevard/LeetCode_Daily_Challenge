# 2023/11/22 Daily challenge
# https://leetcode.com/problems/diagonal-traverse-ii/

from collections import deque
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 对BFS进行初始化，to_visit存储一个tuple，代表nums[i][j]对应的位置
        st = (0, 0)
        to_visit = deque()
        visited = set()
        to_visit.append(st)
        visited.add(st)
        ans = []

        while to_visit:
            cur = to_visit.popleft()
            i, j = cur
            ans.append(nums[i][j])
            # 加入相邻的两个格子，先加下面的再加右边的
            if i + 1 < len(nums) and j < len(nums[i + 1]) and (i + 1, j) not in visited:
                to_visit.append((i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums[i]) and (i, j + 1) not in visited:
                to_visit.append((i, j + 1))
                visited.add((i, j + 1))

        return ans

"""
第一次尝试
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # diag_arr[i]表示在i + 1这条对角线上从上往下的所有数
        diag_arr = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j >= len(diag_arr):
                    diag_arr.append([])
                diag_arr[i + j].append(nums[i][j])

        # 根据diag_arr得到ans
        ans = []
        for diag in diag_arr:
            ans.extend(diag[::-1])
        return ans
"""