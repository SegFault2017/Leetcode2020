#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return True

        seen = {}
        n = len(s)
        for i in range(n):
            if s[i] in seen:
                if t[i] != seen[s[i]]:
                    return False
            else:
                if t[i] in seen.values():
                    return False
                seen[s[i]] = t[i]
        return True
# @lc code=end
