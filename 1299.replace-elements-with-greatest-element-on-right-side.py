#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """ Strategey 1: One pass
        Runtime: O(n), where n is the size of arr
        Space:O(1)

        Args:
            arr (List[int]): list of integers

        Returns:
            List[int]: the modified arr, where every element is the greatest 
            element to the right of the original array.
        """

        n = len(arr)
        curr = 0
        maxR = arr[-1]
        for i in range(n-2, -1, -1):
            curr = arr[i]
            arr[i] = maxR
            maxR = max(maxR, curr)
        arr[n-1] = -1
        return arr
# @lc code=end
