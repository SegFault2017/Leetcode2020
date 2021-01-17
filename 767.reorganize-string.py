#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        """ Strategy 1: Greedy
        Runtime: O(n log(A)), where n is the length of S, A is the size of the alphabet
        Space: O(n)

        Args:
            S (str): the string to be rearranged

        Returns:
            str: the rearranged stirng with no same character are adjacent to each other
        """
        n = len(S)
        counter = Counter(S)
        pq = [(-count, char) for char, count in counter.items()]
        heapq.heapify(pq)

        if any(-count > (n+1)//2 for count, _ in pq):
            return ""

        i = 0
        output = [""] * n

        while pq:
            count, char = heapq.heappop(pq)
            for j in range(-count):
                if i >= n:
                    i = 1
                output[i] = char
                i += 2
        return "".join(output)


# @lc code=end
