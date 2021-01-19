#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        """ Strategy 1: DFS
        Runtime: O(k), where k is the number of valid arrangement
        Space: O(k)

        Args:
            n (int): the integer n

        Returns:
            int: number of beautiful arrangement
        """

        visited = [False] * (n+1)

        def dfs(pos: int) -> int:
            if pos > n:
                return 1

            count = 0
            for i in range(1, n+1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    count += dfs(pos+1)
                    visited[i] = False
            return count

        return dfs(1)

# @lc code=end
