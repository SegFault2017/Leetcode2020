#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        """ Strategy 1: Dynamic Programming
        Runtime: O(n), where n is the size of heights

        Args:
            height (List[int]): height of each bar

        Returns:
            int: the amount of water trapped in the containers formed by bars
        """

        if not height:
            return 0

        n = len(height)
        l_max = [0 if i != 0 else height[0] for i in range(n)]
        r_max = [0 if i != n-1 else height[n-1] for i in range(n)]
        water = 0

        for l in range(1, n):
            l_max[l] = max(height[l], l_max[l-1])

        for r in range(n-2, -1, -1):
            r_max[r] = max(height[r], r_max[r+1])

        for i in range(n):
            water += min(l_max[i], r_max[i]) - height[i]

        return water


# @lc code=end
