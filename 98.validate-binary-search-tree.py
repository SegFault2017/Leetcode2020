#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def validate(self, node: 'TreeNode', low=-math.inf, hi=math.inf) -> bool:
        if not node:
            return True

        if node.val <= low or node.val >= hi:
            return False

        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, hi)

    def isValidBST(self, root: TreeNode) -> bool:
        """Strategy 1: DFS
        Runtime: O(n), where n is the number of nodes
        Space: O(h), where h is the height of the tree

        Args:
            root (TreeNode): [description]

        Returns:
            bool: [description]
        """
        return self.validate(root)

        # @lc code=end
