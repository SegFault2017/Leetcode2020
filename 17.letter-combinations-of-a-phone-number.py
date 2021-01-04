#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

from typing import List

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Strategy 1: Backtracking 
        Runtime: O(3^n * 4^m), where n is the number of 3 letter num in phone, and m is the 4 letter num in phone.
        Space: O(3^n * 4^m)

        Args:
            digits (str): string of digits

        Returns:
            List[str]: list of string combinations
        """

        n = len(digits)
        if n == 0:
            return[]

        letters = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
                   5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}

        output = []

        def dfs(combination: str, next_digit: List[str]) -> None:
            if len(next_digit) == 0:
                output.append(combination)
                return

            for letter in letters[int(next_digit[0])]:
                dfs(combination + letter, next_digit[1:])
            return
        dfs("", digits)
        return output
# @lc code=end
