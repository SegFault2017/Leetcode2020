#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        output = []
        anchor = end = 0

        for i, c in enumerate(S):
            end = max(end, last[c])
            if (i == end):
                output.append(end - anchor + 1)
                anchor = end + 1
        return output

# @lc code=end
