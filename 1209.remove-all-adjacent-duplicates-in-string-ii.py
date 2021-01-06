#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """ Strategy 1: Stack
        Runtime: O(n), where n is the length of s
        Space: O(n)

        Args:
            s (str): the target string 
            k (int): number of adjacent char

        Returns:
            str: the modified string with number of adjacent chars less than k

        """

        stack = [("#", 0)]

        for c in s:
            if c != stack[-1][0]:
                stack.append((c, 1))
            else:
                _, count = stack.pop()
                stack.append((_, count+1))

            if stack[-1][1] == k:
                stack.pop()

        output = ""

        for char, count in stack[1:]:
            output += char * count

        return output

# @lc code=end
