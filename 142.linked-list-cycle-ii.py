#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersect(self, head: ListNode) -> ListNode:
        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return hare

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        """ Strategy 1: Tortoise and hare
        Runtime: O(n)
        Space: O(1)

        Args:
            head (ListNode): the head node of the linked list           

        Returns:
            ListNode: a node where the cycle starts
        """

        if not head:
            return None

        intersect = self.getIntersect(head)
        if not intersect:
            return None
        p1 = head
        p2 = intersect

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

        # @lc code=end
