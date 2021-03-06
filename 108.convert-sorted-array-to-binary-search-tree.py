#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """ Strategy 1: Divide and Conquer
        Runtime: O(n), where n is the size of nums
        Space: O(log n)

        Args:
            nums (List[int]): list of integers

        Returns:
            TreeNode: the root node
        """

        if not nums:
            return None

        def divideConquer(lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            mid = lo + (hi - lo)//2
            node = TreeNode(nums[mid])
            node.left = divideConquer(lo, mid-1)
            node.right = divideConquer(mid+1, hi)
            return node

        return divideConquer(0, len(nums) - 1)
# @lc code=end
