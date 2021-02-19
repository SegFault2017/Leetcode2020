#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        """ Strategy 1: dfs
        Runtime: O(n), where n is the # of nodes in the tree
        Space: O(h), where h is the height of the tree

        Args:
            roots [Node]: the root of the tree
             p [Node]: target 1
             p [Node]: target 2
        Returns:
           [Node]: the lowest common ancestor of p and q.
        """
        output = []

        def dfs(node: 'TreeNode') -> bool:
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            mid = node == p or node == q
            if mid + left + right >= 2:
                output.append(node)
            return mid or left or right
        dfs(root)
        return output[0] if output else None
