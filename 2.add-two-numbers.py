#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ Strategy 1: Linear scan
        Runtime: O(max(n,m))
        Space: O(1)

        Args:
            l1 (ListNode): linked list 1 represents an int in reversed
            l2 (ListNode): linked list 2 represents an int in reversed

        Returns:
            ListNode: the sum of l1 and l2 in reversed
        """

        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        sentinel = ListNode(-1)
        curr = sentinel
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            carry, out = divmod(a+b+carry, 10)

            if l1:
                l1.val = out
                curr.next = l1
            elif l2:
                l2.val = out
                curr.next = l2
            else:
                curr.next = ListNode(1)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sentinel.next
# @lc code=end
