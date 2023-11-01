# 2023/11/1 Daily challenge
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_cnt, max_ls = 0, []
        cur_num, cur_cnt = None, 0
        
        # 中序遍历
        # 在一个有序列表中找到众数是容易的， 而中序遍历让我们把BST当作一个有序列表。
        def inorderTraversal(root):
            nonlocal max_cnt, max_ls, cur_num, cur_cnt
            if not root:
                return 
            inorderTraversal(root.left)

            # 更新cur_num和cur_cnt
            if cur_num != root.val:
                cur_num = root.val
                cur_cnt = 0
            cur_cnt += 1
            
            # 更新max_ls和max_cnt
            if cur_cnt > max_cnt:
                max_cnt = cur_cnt
                max_ls = [cur_num]
            elif cur_cnt == max_cnt:
                max_ls.append(cur_num)

            inorderTraversal(root.right)
        
        inorderTraversal(root)
        
        return max_ls
