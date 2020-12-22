#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """ Inorder + Set
        Runtime: O(n), where n is the number of nodes in the tree

        Args:
            root (TreeNode): the root of the tree
            k (int): the target value

        Returns:
            bool: determine wherther there exist 2 nodes that add up to k
        """

        curr = root
        cache = set()
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if curr.val in cache:
                return True
            cache.add(k - curr.val)
            curr = curr.right
        return False

# @lc code=end
