#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def all_valid_prefixes(self, word: str):
        n = len(word)
        for i in range(n):
            if word[i:] == word[i:][::-1]:
                yield word[:i]
        return

    def all_valid_suffixes(self, word: str):
        n = len(word)
        for i in range(n):
            if word[:i+1] == word[:i+1][::-1]:
                yield word[i+1:]
        return

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reversed_words = {word[::-1]: i for i, word in enumerate(words)}
        output = []

        for i, word in enumerate(words):
            if word in reversed_words and i != reversed_words[word]:
                output.append([i, reversed_words[word]])

            for suffix in self.all_valid_suffixes(word):
                if suffix in reversed_words:
                    output.append([reversed_words[suffix], i])

            for prefix in self.all_valid_prefixes(word):
                if prefix in reversed_words:
                    output.append([i, reversed_words[prefix]])

        return output
# @lc code=end
