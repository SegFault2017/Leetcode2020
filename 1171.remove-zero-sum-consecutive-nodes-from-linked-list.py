#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """Strategy 1: prefix sum + hash map
        Runtime: O(n), where n is the number of nodes
        Space: O(n)

        Args:
            head (ListNode): the head of the node

        Returns:
            ListNode: linked list with no consecutive 0 sum
        """

        sentinel = ListNode(-1001, head)
        curr = head
        prefix = {0: sentinel}
        cumulative = 0

        while curr:
            cumulative += curr.val
            if cumulative in prefix:
                temp = cumulative
                to_remove = prefix[cumulative].next
                while to_remove != curr:
                    temp += to_remove.val
                    del prefix[temp]
                    to_remove = to_remove.next
                prefix[cumulative].next = curr.next

            else:
                prefix[cumulative] = curr
            curr = curr.next

        return sentinel.next
# @lc code=end
