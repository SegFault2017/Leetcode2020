#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Strategy 1: # pointers
        Runtime: O(m+ n), where m is the size of nums1 and n is the size of nums2
        space: O(1)
        """

        p1 = m - 1
        p2 = n-1
        p3 = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1

        nums1[:p2+1] = nums2[:p2+1]

# @lc code=end
