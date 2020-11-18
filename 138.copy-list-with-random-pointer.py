#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.visited = {}
        pass

    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     """ Recursive with hash
    #     Runtime: O(n)
    #     Space: O(n)

    #     """

    #     if not head:
    #         return None

    #     if head in self.visited:
    #         return self.visited[head]

    #     node = Node(head.val, None, None)
    #     self.visited[head] = node
    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)

    #     return node

    def copyRandomList(self, head: 'Node') -> 'Node':
        """Fully weaved link strategy
            Runtime: O(n)
            Space: O(1)
        """

        if not head:
            return None

        # todo: create a weave list
        original = head
        while original:
            cloned = Node(original.val, None, None)
            cloned.next = original.next
            original.next = cloned
            original = cloned.next

        # todo: updates the random pointer for the cloned node in the weave list
        original = head
        while original:
            cloned = original.next
            cloned.random = original.random.next if original.random else None
            original = cloned.next

        # todo: unweave the weave list
        original = head
        cloned = cloned_head = head.next

        while original and cloned:
            original.next = cloned.next
            cloned.next = cloned.next.next if cloned.next else None
            original = original.next
            cloned = cloned.next

        return cloned_head


# @lc code=end
