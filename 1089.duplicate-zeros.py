#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Strategy 1: One Pass
        Do not return anything, modify arr in-place instead.
        """

        n = len(arr)
        count = 0
        for num in arr:
            if num == 0:
                count += 1
        if count == 0:
            return

        first, second = n-1, n-1+count
        arr[:] = arr[:] + [0] * count

        while first > 0:
            if arr[first] != 0:
                arr[first], arr[second] = arr[second], arr[first]
            else:
                second -= 1
            first -= 1
            second -= 1
        for _ in range(len(arr) - n):
            arr.pop()


# @lc code=end
