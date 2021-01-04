class Solution:
    from collections import OrderedDict

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Strategy 1: OrderedDict + indices

        Args:
            s (str): the string
            k (int): the integer k

        Returns:
            int: the longest sustring of s that has at most k distinct character
        """
        n = len(s)
        if n == 0 or k == 0:
            return 0
        if n < k:
            return n

        i = longest = 0
        unique = OrderedDict()

        for j, c in enumerate(s):
            if c in unique:
                del unique[c]
            unique[c] = j

            if len(unique) > k:
                _, indx = unique.popitem(last=False)
                i = indx + 1

            longest = max(longest, j - i + 1)
        return longest
