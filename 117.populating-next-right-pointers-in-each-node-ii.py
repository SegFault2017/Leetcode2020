#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
    def processChild(self, child: 'Node', nxt: 'Node', leftMost: 'Node') -> tuple:
        if child:
            if nxt:
                nxt.next = child
            else:
                leftMost = child
            nxt = child
        return (nxt, leftMost)

    def connect(self, root: 'Node') -> 'Node':
        """ Strategey 1: establish connection using previous node
        Runtime: O(n), where n is the # of nodes
        Space: O(1)

        Args: 
        root: [Node] the root of the tree

        Returns: 
            [Node] the root node
        """
        if not root:
            return None

        leftMost = root

        while leftMost:
            nxt, curr = None, leftMost
            leftMost = None

            while curr:
                nxt, leftMost = self.processChild(curr.left, nxt, leftMost)
                nxt, leftMost = self.processChild(curr.right, nxt, leftMost)
                curr = curr.next
        return root
        # @lc code=end
