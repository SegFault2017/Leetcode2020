#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode) -> (bool, int):
        if not node:
            return True, 0

        left, left_height = self.dfs(node.left)
        if not left:
            return False, left_height

        right, right_height = self.dfs(node.right)
        if not right:
            return False, right_height

        return (abs(left_height - right_height) < 2, 1 + max(left_height, right_height))

    def isBalanced(self, root: TreeNode) -> bool:
        """ DFS
        Runtime: O(n), where n is the number of nodes in the tree
        Space: O(n)

        Args:
            root (TreeNode): the root of the node

        Returns:
            bool: determine where the tree is height-balanced
        """
        return self.dfs(root)[0]


# @lc code=end
