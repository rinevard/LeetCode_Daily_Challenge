# 2023/10/21 Daily challenge
# https://leetcode.com/problems/constrained-subsequence-sum/

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        maxdp = -float('inf')
        # 单调队列，存储dp[j]的下标j
        q, head, tail = [0] * n, 0, 0

        for i in range(n):
            # 如果队列不为空，那么队列的首部就是我们要找的最大的dp[j]的值
            dp[i] = nums[i]
            if head < tail:
                dp[i] = max(dp[i], nums[i] + dp[q[head]])
            
            # 在当前元素比队尾元素大时，弹出队尾元素
            while head < tail and dp[i] >= dp[q[tail - 1]]:
                tail -= 1
            # 当前元素进队列
            if dp[i] > 0:
                q[tail] = i
                tail += 1
                
            # 确保队列首部的元素与当前元素的距离满足约束条件
            while head < tail and q[head] <= i - k:
                head += 1
            
            maxdp = max(maxdp, dp[i])

        return maxdp