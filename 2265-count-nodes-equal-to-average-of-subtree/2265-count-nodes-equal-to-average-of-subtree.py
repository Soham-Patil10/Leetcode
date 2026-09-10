# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        self.count = 0
        def dfs(node):
            if not node:
                return 0, 0
            ls, ln = dfs(node.left)
            rs, rn = dfs(node.right)
            s, n = ls + rs + node.val, ln + rn + 1
            if s // n == node.val:
                self.count += 1
            return s, n
        dfs(root)
        return self.count
        