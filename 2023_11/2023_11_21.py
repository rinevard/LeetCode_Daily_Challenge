# 2023/11/21 Daily challenge
# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = pow(10, 9) + 7
        rev = lambda n: int(str(n)[::-1])
        f = lambda n: n - rev(n)
        count = {}

        # 找到所有的满足 i < j, f(nums[i]) < f(nums[j]) 的 (i, j) 即可
        for num in nums:
            tmp = f(num)
            if tmp not in count:
                count[tmp] = 0
            count[tmp] += 1
        
        ans = 0
        for cnt in count.values():
            ans += (cnt * (cnt - 1)) // 2

        return ans % mod