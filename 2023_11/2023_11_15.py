# 2023/11/15 Daily challenge
# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # 如果追求 O(n)，换成count sort就行，一个小技巧是把大于 len(arr) 的数当作 len(arr).
        arr.sort()
        cur_max = 0
        for num in arr:
            if num > cur_max:
                cur_max += 1

        return cur_max