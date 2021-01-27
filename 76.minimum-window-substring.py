#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

from collections import Counter, defaultdict

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ Strategy 1: 2 pointers + hash
        Runtime: O(n+ m), where n is the length of s and m is the length of t
        Space: O(n+m)

        Args:
            s (str): string 
            t (str): string

        Returns:
            str: determine whethere all characters in t are in s
        """
        if not s or not t:
            return ""

        n = len(s)
        counter = Counter(t)
        window = defaultdict(int)
        start = 0
        shortest = n + 1
        formed, required = 0, len(counter)
        left = right = 0

        while right < n:
            char = s[right]
            window[char] += 1

            if char in counter and counter[char] == window[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]
                window[char] -= 1

                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    start = left

                if char in counter and window[char] < counter[char]:
                    formed -= 1

                left += 1
            right += 1
        return "" if shortest == n+1 else s[start: start + shortest]


# @lc code=end
