#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:

    def all_valid_prefixes(self, word: str) -> str:
        n = len(word)
        for i in range(n):
            sub_word = word[i:]
            reversed = sub_word[::-1]
            if sub_word == reversed:
                yield word[:i]
        pass

    def all_valid_suffixes(self, word: str) -> str:
        n = len(word)
        for i in range(n):
            sub_word = word[:i+1]
            reversed = sub_word[::-1]
            if sub_word == reversed:
                yield word[i+1:]
        pass

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """Strategy 1: Store reverse in Hash
        Runtime: O(n^2 k), where k is the longest length of word

        Args:
            words (List[str]): list of words

        Returns:
            List[List[int]]: list of possible permutation 
        """
        reversed_words = {word[::-1]: i for i, word in enumerate(words)}
        output = []

        for index, word in enumerate(words):
            if word in reversed_words and index != reversed_words[word]:
                output.append([index, reversed_words[word]])

            for suffix in self.all_valid_suffixes(word):
                if suffix in reversed_words:
                    output.append([reversed_words[suffix], index])

            for prefix in self.all_valid_prefixes(word):
                if prefix in reversed_words:
                    output.append([index, reversed_words[prefix]])

        return output
# @lc code=end
