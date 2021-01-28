#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
import heapq
import random
from typing import List

# @lc code=start


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     """ Strategy 1: Heap Sort
    #     Runtime: O(n log (k))
    #     Space: O(log(k))

    #     Args:
    #         nums (List[int]): an array of integers
    #         k (int): a positive integer

    #     Returns:
    #         int: the kth largest
    #     """

    #     heap = []

    #     for num in nums:
    #         if len(heap) < k:
    #             heapq.heappush(heap, num)
    #         else:
    #             if num > heap[0]:
    #                 heapq.heappop(heap)
    #                 heapq.heappush(heap, num)
    #     return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ Strategy 1: Quick Select
        Runtime: O(n)
        Space: O(1)

        Args:
            nums (List[int]): an array of integers
            k (int): a positive integer

        Returns:
            int: the kth largest 
        """
        n = len(nums)

        def partition(left: int, right: int, p_indx: int) -> int:
            pivot = nums[p_indx]
            nums[p_indx], nums[right] = nums[right], nums[p_indx]
            i = left

            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def select(left: int, right: int, kth: int) -> int:
            if left == right:
                return nums[left]

            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)

            if pivot == kth:
                return nums[kth]
            elif kth < pivot:
                return select(left, pivot-1, kth)
            else:
                return select(pivot+1, right, kth)
        return select(0, n-1, n-k)


# @lc code=end
