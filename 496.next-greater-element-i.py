#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Strategy 1: Stack + Hash
        Runtime: O(max(n1,n2)), where n1 is the size of nums1, n2 is the size of nums2
        Space: O(n1+n2)

        Args:
            nums1 (List
            [int]): list of integers
            nums2 (List[int]): list of integers

        Returns:
            List[int]: a list of integers, where each integer is the next greates element in nums2 of nums1, otherwise -1.
        """

        stack = []
        cache = {}

        for x in nums2:
            while stack and stack[-1] < x:
                cache[stack.pop()] = x

            stack.append(x)

        for i in range(len(nums1)):
            if nums1[i] in cache:
                nums1[i] = cache[nums1[i]]
            else:
                nums1[i] = -1
        return nums1

# @lc code=end
