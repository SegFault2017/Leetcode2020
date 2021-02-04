#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """ Strategy 1: Fast and slow
        Runtime: O(n)
        Space: O(1)

        Args:
            head (ListNode): the head of the linked list

        Returns:
            bool: check whether there is a cycle in the linked list
        """

        if not head:
            return None

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
# @lc code=end
