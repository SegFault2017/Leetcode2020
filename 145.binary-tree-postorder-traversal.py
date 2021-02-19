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
        stack = []
        output = []

        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            else:
                output.append(root.val)
                root = None
        return output


# @lc code=end
