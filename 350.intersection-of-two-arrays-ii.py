#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from collections import Counter
from typing import List

# @lc code=start


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Strategey 1: Counter
        Runtime: O(n + m), where n is the size of nums1, m is the size of nums2

        Args:
            nums1 (List[int]): list of integers 
            nums2 (List[int]): list of integers

        Returns:
            List[int]: the intersection of nums1 and nums2
        """
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        output = []

        for num, count in counter1.items():
            if num in counter2:
                minCount = min(count, counter2[num])
                output += [num] * minCount
        return output


# @lc code=end
