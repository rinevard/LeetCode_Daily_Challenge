# 2023/11/25 Daily challenge
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        def calculate_prefix_sums(nums):
            n = len(nums)

            # 计算前缀和
            prefix_sums = [0] * n
            prefix_sums[0] = nums[0]
            for i in range(1, n):
                prefix_sums[i] = prefix_sums[i - 1] + nums[i]

            return prefix_sums

        # 注意到nums是非降序数组
        # ans[i]就是(若干个nums[i]减去左边)加上(右边减去若干个nums[i])
        prefix_sums = calculate_prefix_sums(nums)
        total = prefix_sums[-1]
        n = len(nums)
        ans = []
        for i in range(n):
            left = (i + 1) * nums[i] - prefix_sums[i]
            right = (total - prefix_sums[i]) - (n - i - 1) * nums[i]
            ans.append(left + right)

        return ans
        