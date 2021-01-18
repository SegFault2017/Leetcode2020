#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    #     """ Strategy 1: BFS
    #     Runtime: O(n), where n is the # of nodes in the tree
    #     Space:O(n)

    #     Args:
    #         root (TreeNode): the root of the tree

    #     Returns:
    #         List[List[int]]: nodes in a 2d array in zig zag order
    #     """
    #     if not root:
    #         return None

    #     output = cur_lvl = []
    #     next_lvl = [root]
    #     l_or_r = 0

    #     while next_lvl:
    #         cur_lvl = next_lvl
    #         next_lvl = []
    #         temp = deque()

    #         while cur_lvl:
    #             node = cur_lvl.pop(0)
    #             if not l_or_r:
    #                 temp.append(node.val)
    #             else:
    #                 temp.appendleft(node.val)

    #             for child in [node.left, node.right]:
    #                 if child:
    #                     next_lvl.append(child)

    #         l_or_r ^= 1
    #         output.append(temp)
    #     return output

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """ Strategy 1: DFS
        Runtime: O(n), where n is the # of nodes in the tree
        Space:O(n)

        Args:
            root (TreeNode): the root of the tree

        Returns:
            List[List[int]]: nodes in a 2d array in zig zag order
        """

        output = []

        def dfs(node: 'TreeNode', level: int) -> None:
            if not node:
                return

            if level >= len(output):
                output.append(deque([node.val]))
            else:
                if level % 2:
                    output[level].appendleft(node.val)
                else:
                    output[level].append(node.val)

            for child in [node.left, node.right]:
                if child:
                    dfs(child, level+1)
            return
        dfs(root, 0)
        return output


# @lc code=end
