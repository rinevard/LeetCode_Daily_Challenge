# 2023/11/23 Daily challenge
# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 该函数判断一个数组是否重新排列构成等差数列
        def check(arr):
            # 构建等差数列判断两个数组中的元素是否相同 O(n)
            max_num, min_num = max(arr), min(arr)
            det = (max_num - min_num) // (len(arr) - 1)
            arithmetic_arr = [min_num + i * det for i in range(len(arr))]
            return set(arithmetic_arr) == set(arr)

            # 先排序遍历并判断相邻元素的差 O(nlogn)
            sorted_arr = sorted(arr)
            det = sorted_arr[1] - sorted_arr[0]
            for i in range(len(sorted_arr) - 1):
                if det != sorted_arr[i + 1] - sorted_arr[i]:
                    return False
            return True

        ans = []
        for left, right in zip(l, r):
            ans.append(check(nums[left: right + 1]))

        return ans
        