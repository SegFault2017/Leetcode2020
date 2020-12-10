#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List


class Solution:
    import heapq
    ListNode.__lt__ = lambda self, other: self.val < other.val

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """ Streategy 1: Priority Queue
        RunTime: O(N log k)
        Space: O(k)


        Args:
            lists (List[ListNode]): list of linked lists

        Returns:
            ListNode: the merged linked lists
        """

        if not lists:
            return None

        heap = []
        merged = curr = ListNode(-1)

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))

        while heap:
            _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        return merged.next

# @lc code=end
