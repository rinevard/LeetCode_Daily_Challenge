# 2023/10/30 Daily challenge
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # radix sort
        num_of_one_ls = [[] for _ in range(15)] # 2^14 > 10000 > 2^13

        def compute_num_of_one(num):
            cnt = 0
            while num != 0:
                rest = num % 2
                cnt += rest
                num //= 2

            return cnt

        # 初始化列表（根据二进制中1的数量）
        for num in arr:
            num_of_one_ls[compute_num_of_one(num)].append(num)

        ans = []
        # 逐个排序
        for ls in num_of_one_ls:
            ls.sort()
            ans.extend(ls)

        return ans