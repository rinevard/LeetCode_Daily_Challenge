# 2023/10/28 Daily challenge
# https://leetcode.com/problems/count-vowels-permutation/description/
# 基于矩阵的解法（a Matrix solution）请查看
# https://leetcode.com/problems/count-vowels-permutation/solutions/3040891/python-4-solutions-slowly-getting-better-thought-process-beats-99/?orderBy=hot

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7

        end_with_a, end_with_e, end_with_i, end_with_o, end_with_u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a = (end_with_e + end_with_i + end_with_u) % mod
            e = (end_with_a + end_with_i) % mod
            i = (end_with_e + end_with_o) % mod
            o = end_with_i
            u = (end_with_i + end_with_o) % mod
            
            end_with_a, end_with_e, end_with_i, end_with_o, end_with_u = a, e, i, o, u

        return (end_with_a + end_with_e + end_with_i + end_with_o + end_with_u) % mod