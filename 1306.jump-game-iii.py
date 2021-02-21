#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
from typing import List


class Solution:
    # def canReach(self, arr: List[int], start: int) -> bool:
    #     """ Strategy 1: DFS
    # Runtime :O(n), where n is size of arr
    # Space:O(n)

    #     Args:
    #         arr (List[int]): list of non-negative integers
    #         start (int): staring index

    #     Returns:
    #         bool: determine whether we can reach to any index with a value,0,
    #         from the staring index
    #     """

    #     n = len(arr)
    #     jumps = arr[:]

    #     def dfs(begin: int) -> bool:
    #         if begin < 0 or begin >= n or jumps[begin] < 0:
    #             return False
    #         if jumps[begin] == 0:
    #             return True
    #         jumps[begin] *= -1
    #         return dfs(begin - jumps[begin]) or dfs(begin + jumps[begin])
    #     return dfs(start)

    def canReach(self, arr: List[int], start: int) -> bool:
        """ Strategy 1: BFS
        Runtime: O(n)
        Space: O(n)

        Args:
            arr (List[int]): list of non-negative integers
            start (int): staring index

        Returns:
            bool: determine whether we can reach to any index with a value,0, 
            from the staring index
        """

        n = len(arr)
        q = [start]
        visited = arr[:]
        visited[start] *= -1

        def isValid(idx: int) -> bool:
            return 0 <= idx < n and visited[idx] >= 0

        while q:
            idx = q.pop(0)

            for i in [idx - arr[idx], idx + arr[idx]]:
                if isValid(i):
                    visited[i] *= -1
                    if arr[i] == 0:
                        return True
                    q.append(i)
        return False


# @lc code=end
