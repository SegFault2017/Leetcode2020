#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import namedtuple
from typing import NamedTuple


class Solution:
    def lcaDeepestLeaves(self, root: 'TreeNode') -> 'TreeNode':
        """ Strategy 1: Dfs
        Runtime: O(n), where n is the number of nodes
        Space: O(h), where h is the height of the tree

        Args:
            root [TreeNode]: the root node

        Returns:
            [TreeNode]: the lca of deepest node
        """

        output = namedtuple("output", ("node", "dist"))

        def dfs(node: 'TreeNode') -> NamedTuple:
            if not node:
                return output(None, 0)

            left, right = dfs(node.left), dfs(node.right)
            if left.dist > right.dist:
                return output(left.node, left.dist+1)
            if right.dist > left.dist:
                return output(right.node, right.dist+1)
            return output(node, left.dist+1)

        return dfs(root).node

        # @lc code=end
