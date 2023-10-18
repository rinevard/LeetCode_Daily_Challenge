# 2023/10/16 Daily challenge
# https://leetcode.com/problems/validate-binary-tree-nodes/
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        children = set(leftChild + rightChild)
        # 找到可能的根节点
        for i in range(n):
            if i not in children:
                root = i

        visited = [False] * n
        num = 0
        cur_tree = [root]
        while cur_tree:
            curr = cur_tree.pop()
            if visited[curr]:
                return False

            visited[curr] = True
            num += 1

            l, r = leftChild[curr], rightChild[curr]
            if l != -1:
                cur_tree.append(l)
            if r != -1:
                cur_tree.append(r)
        
        return num == n