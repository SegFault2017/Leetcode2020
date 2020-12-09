#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Strategy1: In Place linking method   
        Runtime: O(n+m), where n is the size of l1 and m is the size of l2
        Space: O(1)
        Args:
            l1 (ListNode): linked list 1
            l2 (ListNode): linked list 2

        Returns:
            ListNode: merged linked list of 1 and 2
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        merged = curr = ListNode(-1)
        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next

        if curr1:
            curr.next = curr1
        else:
            curr.next = curr2

        return merged.next


# @lc code=end
