# 2023/11/18 Daily challenge
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_freq = 0

        for right in range(len(nums)):
            total += nums[right]
            operations = nums[right] * (right - left + 1) - total

            # 当需要的操作数大于 k 时，移动左指针
            while operations > k:
                total -= nums[left]
                left += 1
                operations = nums[right] * (right - left + 1) - total

            max_freq = max(max_freq, right - left + 1)

        return max_freq
