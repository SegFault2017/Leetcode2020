#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ Strategy : Linear scan + remove sublist(duplicates)
        Runtime: O(n), where n is the # of nodes
        Space: O(1)

        Args:
            head (ListNode): the head of the linked list    

        Returns:
            ListNode: linked list with no duplicates
        """

        sentinel = ListNode(-1, head)
        pred = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinel.next
# @lc code=end
