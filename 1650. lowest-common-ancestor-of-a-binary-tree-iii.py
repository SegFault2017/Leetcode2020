"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """ Strategy 1: Check parent linearly
        Runtime: O(n), where n is the # of nodes in the tree
        Space:O(n)

        Returns:
            Node: the root of the lcs
        """
        ancestor = set()

        while p:
            ancestor.add(p)
            p = p.parent

        while q not in ancestor:
            q = q.parent
        return q
