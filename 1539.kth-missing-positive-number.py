#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """ Strategy 1: Binary Search
        Runtime: O(log(n))
        Space: O(1)

        Args:
            arr (List[int]): increasing order of arr
            k (int): number of missing integers

        Returns:
            int: the kth missing number in arr
        """

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left)//2
            if arr[mid] - mid - 1 < k:
                left = mid+1
            else:
                right = mid - 1
        return left + k
# @lc code=end
