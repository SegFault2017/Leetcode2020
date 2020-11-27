#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     """Strategy 1: Recursive
    # Runtime: O(n), where n is # of tree
    # Space : O(h), h is the height of the tree

    #     Args:
    #         root (TreeNode): root of the tree

    #     Returns:
    #         List[int]: return a list of nodes in order
    #     """
    #     if not root:
    #         return []

    #     output = []

    #     def traverse(node: TreeNode) -> None:
    #         if not node:
    #             return

    #         traverse(node.left)
    #         output.append(node.val)
    #         traverse(node.right)

    #     traverse(root)
    #     return output

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """Strategy 2: Iterative
        Runtime : O(N), where N is the number of nodes
        Space: O(h), where h is the height of the tree

        Args:
            root (TreeNode): the root of the tree

        Returns:
            List[int]: a list of nodes in order
        """

        if not root:
            return root

        output = []
        curr = root
        stack = []

        # [2]
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if len(stack) == 0:
                return output
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right

        return output
        # @lc code=end
