#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.total = 0
        return

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """ Strategey 1: Dynamic programming
        Runtime: O(n), where n is the size of the tree
        Space: O(n)

        Args:
            root (TreeNode): the root of the tree

        Returns:
            TreeNode: the root of Gst, every key of the original BST is changed to the 
            original key + sum of all keys > the original key in BST.
        """

        if root:
            self.bstToGst(root.right)
            self.total += root.val
            root.val = self.total
            self.bstToGst(root.left)
        return root
# @lc code=end
