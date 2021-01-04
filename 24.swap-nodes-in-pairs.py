#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     """ Iterative
    #     Runtime: O(n)
    #     Space: O(1)

    #     Args:
    #         head (ListNode): the head of the linked list

    #     Returns:
    #         ListNode: pairs of nodes are swapped in the linked list
    #     """

    #     if not head:
    #         return None

    #     sentinel = ListNode(-1, head)
    #     first = head
    #     second = first.next
    #     prev = sentinel

    #     while first and second:
    #         temp = second.next
    #         second.next = first
    #         first.next = temp
    #         prev.next = second
    #         prev = first

    #         first = first.next
    #         if first:
    #             second = first.next
    #     return sentinel.next

    def swapPairs(self, head: ListNode) -> ListNode:
        """ Recursive
        Runtime: O(n)
        Space: O(n)

        Args:
            head (ListNode): the head of the linked list

        Returns:
            ListNode: pairs of nodes are swapped in the linked list
        """
        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first
        return second


# @lc code=end
