#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """ Strategy 1: DFS
        Runtime: O(n), where n is the # of nodes in the tree
        Space: O(n)

        Args:
            root (TreeNode): the root node
            low (int): the lower bound
            high (int): the upper bound

        Returns:
            TreeNode: the root of the modified tree
        """

        if not root:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        elif root.val < low:
            return self.trimBST(root.right, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
# @lc code=end
