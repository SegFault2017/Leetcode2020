#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ Strategy 1: Sorting
        Runtime: O(n log n), where n is the length of intervals
        Space: O(log n )
        Args:
            intervals (List[List[int]]): list of [start, end], where start is 
            the staring time of an interval, and end is the closing time of an interval

        Returns:
            List[List[int]]: list of merged intervals
        """

        n = len(intervals)
        if n == 0:
            return 0

        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# @lc code=end
