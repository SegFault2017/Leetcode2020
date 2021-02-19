#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # def connect(self, root: 'Node') -> 'Node':
    #     """ Strategey 1: bfs
    #     Runtime: O(n), where n is the nodes in the tree
    #     Space: O(l), where l is the max number of nodes in a level of all
    #     Args:
    #         root: [Node]: the root node
    #     Returns:
    #         [type]: the root node
    #     """

    #     if not root:
    #         return None

    #     cur_lvl = []
    #     nxt_lvl = [root]

    #     while nxt_lvl:
    #         cur_lvl = nxt_lvl
    #         nxt_lvl = []
    #         prev = TreeNode(-1)
    #         while cur_lvl:
    #             node = cur_lvl.pop(0)
    #             prev.next = node
    #             prev = node
    #             for child in [node.left, node.right]:
    #                 if child:
    #                     nxt_lvl.append(child)

    #     return root

    def connect(self, root: 'Node') -> 'Node':
        """ Strategey 1: establish connection using previous node
        Runtime: O(n), where n is the nodes in the tree
        Space: O(1)
        Args:
            root: [Node]: the root node
        Returns:
            [type]: the root node
        """
        if not root:
            return None

        leftMost = root

        while leftMost.left:
            head = leftMost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftMost = leftMost.left
        return root
        # @lc code=end
