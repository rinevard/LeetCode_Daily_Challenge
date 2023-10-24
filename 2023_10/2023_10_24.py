# 2023/10/24 Daily challenge
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = queue.Queue()
        cur_row_depth = 0
        cur_row_max = -float('inf')
        q.put((root, cur_row_depth))

        while not q.empty():
            node, tmp_depth = q.get()
            l, r = node.left, node.right

            if l: q.put((l, tmp_depth + 1))
            if r: q.put((r, tmp_depth + 1))

            if tmp_depth == cur_row_depth:
                cur_row_max = max(cur_row_max, node.val)
            else:
                ans.append(cur_row_max)
                cur_row_depth = tmp_depth
                cur_row_max = node.val

        # 把最后一行的最大值也加入到ans中
        ans.append(cur_row_max)
        return ans

# 另一种可行方案(from chatgpt)
"""
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return
            # 如果当前深度大于结果数组的长度，说明这是新的一行，初始化这一行的最大值为当前节点的值
            if depth == len(res):
                res.append(node.val)
            else:
                # 更新这一行的最大值
                res[depth] = max(res[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        res = []
        dfs(root, 0)
        return res
"""