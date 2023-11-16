# 2023/11/16 Daily challenge
# https://leetcode.com/problems/find-unique-binary-string/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # second_sol
        # make sure that ans[i] != nums[i][i]
        ans = ''
        binary_len = len(nums[0])
        for i in range(binary_len):
            if i < len(nums):
                ans += str((int(nums[i][i]) + 1) % 2)
            else:
                ans += '0'
        return ans


"""
first_sol
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = 0
        num_set = set(nums)

        def binary_str(num, length):
            if num == 0: return '0' * length
            ans_len = 0
            ans = ''
            while num > 0:
                mod = num % 2
                num //= 2
                ans += str(mod)
                ans_len += 1
            return '0' * (length - ans_len) + ans[::-1]

        while binary_str(ans, len(nums[0])) in num_set:
            ans += 1
        
        return binary_str(ans, len(nums[0]))

"""
