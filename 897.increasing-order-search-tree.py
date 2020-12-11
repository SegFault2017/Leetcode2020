#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Strategy 1: In order traversal
        Runtime: O(n)
        Space: O(h), where h is the height of the tree
        Args:
            root (TreeNode): the root of the tree

        Returns:
            TreeNode: Return an in order tree with 
        """

        if not root:
            return

        output = curr = TreeNode(-1)

        def inOrder(node: TreeNode) -> None:
            nonlocal curr
            if not node:
                return

            inOrder(node.left)
            curr.right = node
            node.left = None
            curr = curr.right
            inOrder(node.right)

        inOrder(root)
        return output.right

# @lc code=end
