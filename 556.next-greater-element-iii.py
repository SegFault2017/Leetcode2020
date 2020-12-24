#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
from functools import reduce


class Solution:
    from functools import reduce

    def nextGreaterElement(self, n: int) -> int:
        """ Strategy 1: Swap and reverse
        Runtime: O(n), where n is the number of digits in n
        Space: O(1)

        Args:
            n (int): the number 

        Returns:
            int: the next greatest number
        """

        s = list(map(int, str(n)))
        size = len(s)
        i, j = size-2, size-1

        while i >= 0 and s[i+1] <= s[i]:
            i -= 1

        if i < 0:
            return -1

        while j >= 0 and s[j] <= s[i]:
            j -= 1

        s[j], s[i] = s[i], s[j]

        s[i+1:] = s[i+1:][::-1]

        num = reduce(lambda x, y: 10 * x + y, s)
        return num if num < 2 ** 31 - 1 else -1


# @lc code=end
