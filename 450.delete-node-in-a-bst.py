#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def successor(self, node: 'TreeNode') -> int:
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def preSuccessor(self, node: 'TreeNode') -> int:
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: 'TreeNode', key: int) -> 'TreeNode':
        """ Strategy 1: Dfs
        Runtime: O(h), where h is the height of the tree
        Space: O(height)

        Args:
            root (TreeNode): the root of the tree2
            key (int): the target value 

        Returns:
            TreeNode: the modified tree without the target node
        """

        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right and not root.left:
                root = None
            elif root.left:
                root.val = self.preSuccessor(root)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

        return root


# @lc code=end
