# 2023/10/26 Daily challenge
# https://leetcode.com/problems/binary-trees-with-factors/

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n, mod = len(arr), pow(10, 9) + 7
        ans = 0
        arr.sort()
        trees = {val: 0 for val in arr} # trees[val]表示根节点为val的树的数量

        for i in range(n):
            # 可以是一个只有一个根节点的树
            trees[arr[i]] += 1
            for j in range(i):
                # 如果有子树， 那么子树的根节点的值的乘积一定是原树的根节点的值
                # 且子树的根节点的值小于原树的值
                # 判断子树有多少种组成方法即可
                if arr[i] % arr[j] == 0 and arr[i] / arr[j] in trees:
                    trees[arr[i]] += trees[arr[j]] * trees[arr[i] / arr[j]]
            ans = (ans + trees[arr[i]]) % mod
    
        return ans

