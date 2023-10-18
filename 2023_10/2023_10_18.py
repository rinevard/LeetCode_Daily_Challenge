# 2023/10/16 Daily challenge
# https://leetcode.com/problems/parallel-courses-iii/description/
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        # 为了学完child这节课，我们需要学完所有的parent。
        for parent, child in relations:
            graph[child - 1].append(parent - 1)

        dp = [-1] * n

        def miniTime(course):
            # 该函数返回学完以course为终点的课需要的最小时间

            if dp[course] != -1:
                return dp[course]

            # 为了学完这节课，我们需要先学完所有的parent
            max_parent_time = 0
            for parent in graph[course]:
                max_parent_time = max(max_parent_time, miniTime(parent))

            dp[course] = max_parent_time + time[course]
            return dp[course]

        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, miniTime(course))

        return overall_min_time