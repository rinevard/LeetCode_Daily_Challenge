# 2023/10/22 Daily challenge
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_val = nums[k]
        left, right = k, k
        ans = 0

        # 注意这样一个事实：假设我们在(i, j)处取得最大分数，那么min(nums[i:j+1])一定大于nums[i-1]和nums[j+1]
        # 否则，我们可以令i = i - 1或者令j = j + 1
        while left >= 0 or right < n:
            while left >= 0 and nums[left] >= min_val:
                left -= 1
            while right < n and nums[right]>= min_val:
                right += 1

            ans = max(ans, (right - left + 1 - 2) * min_val)
            min_val = max(nums[left] if left >= 0 else 0, nums[right] if right < n else 0)
       
        return ans
