#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ Strategey 1: DFS
        Runtime: O(n), where n is the number of nodes
        Sapce: O(1)

        Args:
            root [TreeNode]: the root of the tree
            p [TreeNode]: target 1
            q [TreeNode]: target 2

        Returns:
            [TreeNode]: the lca of p and q
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# @lc code=end
