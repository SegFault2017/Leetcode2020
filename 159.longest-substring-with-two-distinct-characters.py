class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """Strategy 1: Sliding Window

        Args:
            s (str): a string

        Returns:
            int: the length of the longest substring with two distinct characters
        """

        n = len(s)
        k = 2
        if n < k:
            return n

        i = j = longest = 0
        unique = set()

        while j < n:
            unique[s[j]] = j
            j += 1

            if n == k+1:
                # find the most recent characters
                del_inx = min(unique.values())
                del unique[s[del_inx]]
                i = del_inx + 1
            longest = max(longest, j - i)

        return longest
