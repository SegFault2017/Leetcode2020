#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        a_ptr = headA
        b_ptr = headB

        while a_ptr != b_ptr:
            if not a_ptr:
                a_ptr = headB
            else:
                a_ptr = a_ptr.next

            if not b_ptr:
                b_ptr = headA
            else:
                b_ptr = b_ptr.next

        return a_ptr
# @lc code=end
