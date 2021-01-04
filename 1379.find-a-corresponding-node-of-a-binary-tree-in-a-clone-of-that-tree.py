#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """ Strategy 1: DFS
        Runtime: O(n)
        Space: O(n)

        Args:
            original (TreeNode): the original tree
            cloned (TreeNode): the cloned tree
            target (TreeNode): the target node

        Returns:
            TreeNode: return a node in cloned tree that is equal to the target node
        """

        def dfs(o_node: 'TreeNode', c_node: 'TreeNode') -> None:
            if not o_node or not c_node:
                return None

            if o_node is target:
                return c_node

            return dfs(o_node.left, c_node.left) or dfs(o_node.right, c_node.right)
        return dfs(original, cloned)
# @lc code=end
