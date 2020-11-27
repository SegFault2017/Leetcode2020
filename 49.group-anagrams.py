#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Strategy 1: Hash + Array
        Runtime: O(n K), where n is the number of words in strs, k is the length of the longest word
        Space: O(n k)

        Args:
            strs (List[str]): A list of words

        Returns:
            List[List[str]]: list of grouped anagrams
        """

        anagrams = defaultdict(list)

        for word in strs:
            alphabet_count = [0] * 26
            for c in word:
                alphabet_count[ord(c) - ord('a')] += 1
            anagrams[tuple(alphabet_count)].append(word)

        return anagrams.values()

# @lc code=end
