#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """ Strategy 1: Binary Search
        Runtime: O(log(n))
        Space:O(1)

        Args:
            letters (List[str]): a list of lowercase characters
            target (str): the target character

        Returns:
            str: return the smallest letter in letters that is greater than target
        """

        n = len(letters)
        lo, hi = 0, n-1
        if letters[hi] <= target:
            return letters[0]

        while lo <= hi:
            mid = lo + (hi - lo)//2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return letters[lo]

# @lc code=end
