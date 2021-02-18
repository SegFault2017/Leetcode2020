#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     """ Stragtegy 1: Iterative
    #     Runtime: O(n), where n is the number of nodes
    #     Space:O(n)

    #     Args:
    #         root (TreeNode): the root of the tree.

    #     Returns:
    #         List[int]: a list of nodes in preorder.
    #     """

    #     if not root:
    #         return []
    #     stack = [root]
    #     output = []

    #     while stack:
    #         node = stack.pop()
    #         output.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return output

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ Stragtegy 1: Iterative
        Runtime: O(n), where n is the number of nodes
        Space:O(n)

        Args:
            root (TreeNode): the root of the tree.

        Returns:
            List[int]: a list of nodes in preorder.
        """

        if not root:
            return []
        output = [root.val]
        output += self.preorderTraversal(root.left)
        output += self.preorderTraversal(root.right)
        return output

# @lc code=end
