#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """ Strategy 1: Iteractive
        Runtime: O(n), where n is the number of nodes is the tree
        Space: O(h), where h is the height of the tree

        Args:
            root (TreeNode): the root of the tree
            sum (int): the target sum value 

        Returns:
            bool: determine wherthere there exist a path the sums up to sum
        """
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True

            if node.left:
                stack.append((node.left, curr_sum - node.left.val))

            if node.right:
                stack.append((node.right, curr_sum - node.right.val))

        return False


# @lc code=end
