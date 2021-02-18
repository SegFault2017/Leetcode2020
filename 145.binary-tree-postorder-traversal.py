#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     """ Strategey 1: DFS
    #     Runtime: O(n), where n is the number of nodes
    #     Space: O(n)

    #     Args:
    #         root (TreeNode): root node

    #     Returns:
    #         List[int]: list of nodes in preorder order.
    #     """

    #     if not root:
    #         return []

    #     output = []
    #     output += self.postorderTraversal(root.left)
    #     output += self.postorderTraversal(root.right)
    #     output.append(root.val)
    #     return output

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """ Strategey 1: Iterative
        Runtime: O(n), where n is the number of nodes
        Space: O(n)

        Args:
            root (TreeNode): root node

        Returns:
            List[int]: list of nodes in preorder order.
        """

        if not root:
            return []
        stack = [root]
        output = []

        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output[::-1]
# @lc code=end
