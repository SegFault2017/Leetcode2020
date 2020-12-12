#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """Strategy 1: Fast and slow Runner
        Runtime: O(n), where n is the # of nodes in the list
        Space: O(1)
        Args:
            head (ListNode): the head of the list

        Returns:
            ListNode: the middle node
        """

        if not head:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# @lc code=end
