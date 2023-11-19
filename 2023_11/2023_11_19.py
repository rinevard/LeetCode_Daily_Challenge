# 2023/11/19 Daily challenge
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # 假设排序后的数组共有 m 个不同元素，分别是 x_1, ..., x_m
        # 每个元素数量是 count_1, ..., count_m
        # 我们把最大的变成次大的，再把次大的变成次次大的
        # 最终结果为 sum((j - 1) * count_j) j from 1 to m
        nums.sort()
        differ_idx = 0
        cur_num = nums[0]
        ans = 0
        for num in nums:
            if num != cur_num:
                differ_idx += 1
                cur_num = num
            ans += differ_idx
    
        return ans