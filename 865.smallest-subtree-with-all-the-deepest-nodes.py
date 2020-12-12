#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import namedtuple


class Solution:
    from collections import namedtuple

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """Strategy 1: DFS
        Runtime: O(N), where N is the number of nodes in the tree
        Space: O(N)

        Args:
            root (TreeNode): the root of the tree

        Returns:
            TreeNode: the smallest subtree which has deepest height
        """
        output = namedtuple("output", ("node", "dist"))

        def dfs(node: 'TreeNode') -> tuple:
            if not node:
                return output(None, 0)

            left, right = dfs(node.left), dfs(node.right)
            if left.dist > right.dist:
                return output(left.node, left.dist+1)
            if right.dist > left.dist:
                return output(right.node, right.dist+1)
            return output(node, left.dist+1)
        return dfs(root).node


# @lc code=end
