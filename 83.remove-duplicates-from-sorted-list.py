#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Strategy 1: 2 pointers

        Args:
            head (ListNode): the head node

        Returns:
            ListNode: The modified linked list
        """
        if not head:
            return None

        curr = prev = head
        slow = fast = head.next
        count = 1

        while fast:
            if curr.val == fast.val:
                count += 1
            else:
                count = 1

            if count <= 1:
                slow.val = fast.val
                slow = slow.next
                prev = prev.next
            fast = fast.next
            curr = curr.next
        if prev:
            prev.next = None
        return head


# @lc code=end
