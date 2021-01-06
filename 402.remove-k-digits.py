#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """ Strategy 1: Stack
        Runtime: O(n), where n is the length of num
        Space: O(n)

        Args:
            num (str): the number
            k (int): the number of digits should be removed

        Returns:
            str: the modified number after kth removal.
        """

        stack = []

        for digit in num:
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k else stack

        return "".join(stack).lstrip("0") or "0"


# @lc code=end
