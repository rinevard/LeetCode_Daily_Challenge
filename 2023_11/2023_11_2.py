# 2023/11/2 Daily challenge
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        dp_sum = {}
        dp_num = {}

        def sum(root):
            if root == None:
                return 0
            if root not in dp_sum:
                dp_sum[root] = root.val + sum(root.left) + sum(root.right)
            return dp_sum[root]

        def num(root):
            if root == None:
                return 0
            if root not in dp_num:
                dp_num[root] = 1 + num(root.left) + num(root.right)
            return dp_num[root]

        def update(root):
            nonlocal cnt
            if root == None:
                return
            cnt += (root.val == sum(root) // num(root))
            update(root.left)
            update(root.right)

        update(root)
        return cnt