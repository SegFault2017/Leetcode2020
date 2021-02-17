#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Strategy 1: one pass
        Runtime: O(n), where n is the number of elements in the arr
        Space: O(1)
        Args:
            arr (List[int]): list of integer

        Returns:
            bool: whether the array is a valid mountain or not

        """

        n = len(arr)
        i = 0

        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1

        if i == 0 or i == n-1:
            return False

        while i+1 < n and arr[i] > arr[i+1]:
            i += 1

        return i == n-1
# @lc code=end
