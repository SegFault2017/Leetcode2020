#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

from collections import deque


# @lc code=start
class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     """ Strategey 1: Deque
    #     Runtime: O(n), where n is the size of nums
    #     Space: O(n)

    #     Args:
    #         nums (List[int]): list of integers to
    #         k (int): window size

    #     Returns:
    #         List[int]: list of maximums of all (n-k+1) windows with size k
    #     """

    #     n = len(nums)
    #     if n * k == 0:
    #         return []

    #     dq = deque()

    #     def cleanDeque(idx: int) -> None:
    #         if dq and dq[0] == idx - k:
    #             dq.popleft()

    #         while dq and nums[i] > nums[dq[-1]]:
    #             dq.pop()
    #         return

    #     for i in range(k):
    #         cleanDeque(i)
    #         dq.append(i)

    #     maximums = [nums[dq[0]]]

    #     for i in range(k, n):
    #         cleanDeque(i)
    #         dq.append(i)
    #         maximums.append(nums[dq[0]])
    #     return maximums

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ Strategey 1: Dynamic Programming
        Runtime: O(n), where n is the size of nums 
        Space: O(n)

        Args:
            nums (List[int]): list of integers to
            k (int): window size 

        Returns:
            List[int]: list of maximums of all (n-k+1) windows with size k
        """

        n = len(nums)
        if k * n == 0:
            return []

        left, right = [0] * n, [0]*n
        left[0] = nums[0]
        right[n-1] = nums[n-1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])

            j = n - i - 1

            if (j+1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        maximums = []

        for i in range(n-k+1):
            maximums.append(max(left[i+k-1], right[i]))
        return maximums

        # @lc code=end
