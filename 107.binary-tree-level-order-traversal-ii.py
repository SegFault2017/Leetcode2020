#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """ Strategey 1: BFS
          Runtime: O(n), where n is the number of nodes in the tree
         Space:O(n)
          Args:
              root (TreeNode): the root node

          Returns:
              List[List[int]]: list of node val in level order from left to right.
          """

        if not root:
            return []

        output = deque()
        cur_lvl = []
        nxt_lvl = [root]
        temp = [root.val]

        while nxt_lvl:
            output.appendleft(temp)
            cur_lvl = nxt_lvl
            nxt_lvl = []
            temp = []

            while cur_lvl:
                node = cur_lvl.pop(0)
                for child in [node.left, node.right]:
                    if child:
                        temp.append(child.val)
                        nxt_lvl.append(child)
        return output
        # @lc code=end
