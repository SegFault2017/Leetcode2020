#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     """ Strategy 1: Prefix sum + DFS
    #     Runtime: O(n), where n is the number of nodes
    #     Space: O(h), where h is the height of the tree

    #     Args:
    #         root (TreeNode): the root of the tree
    #         sum (int): the target value

    #     Returns:

    #         int: number of paths that sums up to sum from any ancestor to its descendent
    #     """

    #     prefix_sum = defaultdict(int)
    #     prefix_sum[0] = 1

    #     def dfs(node: 'TreeNode', pre_sum: int) -> int:
    #         if not node:
    #             return 0

    #         curr = pre_sum + node.val
    #         paths = prefix_sum[curr - sum]
    #         prefix_sum[curr] += 1
    #         paths += dfs(node.left, curr) + dfs(node.right, curr)
    #         prefix_sum[curr] -= 1
    #         return paths

    #     return dfs(root, 0)

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """ Strategy 1: Prefix sum + Iterative
        Runtime: O(n), where n is the number of nodes
        Space: O(h), where h is the height of the tree


        Args:
            root (TreeNode): the root of the tree
            sum (int): the target value

        Returns:
            int: number of paths that sums up to sum from any ancestor to its descendent
        """


# @lc code=end
