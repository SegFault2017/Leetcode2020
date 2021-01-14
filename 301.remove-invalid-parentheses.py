#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, string: str) -> bool:
        count = 0
        for b in string:
            count += (b == "(")
            count -= (b == ")")
            if count < 0:
                return False
        return count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        """ Strategy 1: Backtrack
        Runtime:O(2^(l+r)), where l is the # of (, r is the # of )
        Spacetime:O(2^(l+r))

        Args:
            s (str): the string s

        Returns:
            List[str]: all possible valid parenthese
        """

        # count # of unbalanced parenthese
        left = right = 0
        left_b = "("
        right_b = ")"
        output = []

        for b in s:
            left += (b == left_b)
            if left == 0:
                right += (b == right_b)
            else:
                left -= (b == right_b)

        def dfs(string: str, start: int, l: int, r: int) -> None:
            if l == 0 and r == 0 and self.isValid(string):
                output.append(string)
                return

            n = len(string)
            for i in range(start, n):
                if i != start and string[i] == string[i-1]:
                    continue
                if string[i] == left_b or string[i] == right_b:
                    temp = string
                    temp = temp[:i] + temp[i+1:]
                    if r > 0:
                        dfs(temp, i, l, r-1)
                    elif l > 0:
                        dfs(temp, i, l-1, r)
            return

        dfs(s, 0, left, right)
        return output


# @lc code=end
