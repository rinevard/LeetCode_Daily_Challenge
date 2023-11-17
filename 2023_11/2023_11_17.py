# 2023/11/17 Daily challenge
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[0] + nums[-1]
        n = len(nums)
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])

        return ans