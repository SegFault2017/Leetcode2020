#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """Strategy 1: Linear Scan

        Args:
            num1 (str): number 1 in string
            num2 (str): number 2 in string      

        Returns:
            str: num1 + num2 in string
        """

        n = len(num1) - 1
        m = len(num2) - 1
        output = ""
        carry = 0

        while m >= 0 or n >= 0:
            x1 = ord(num1[n]) - ord('0') if n >= 0 else 0
            x2 = ord(num2[m]) - ord('0') if m >= 0 else 0
            print(x1, x2)
            output = str((x1 + x2 + carry) % 10) + output
            carry = (x1 + x2 + carry) // 10
            n -= 1
            m -= 1

        return "1" + output if carry > 0 else output

# @lc code=end
