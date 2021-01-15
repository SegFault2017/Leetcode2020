#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ Strategy 1: BFS
        Runtime: O(n * m ^2), where n is the number of words, m is the length of a word
        Space: O(n * m ^2)

        Args:
            beginWord (str): the word to begin with
            endWord (str): the destination word
            wordList (List[str]): list of words

        Returns:
            int: # of transformations
        """
        # bases cases
        if not endWord or not beginWord or len(beginWord) != len(endWord) \
                or endWord not in wordList or not wordList:
            return 0
        length = len(beginWord)
        wildcards = defaultdict(list)
        level = 0

        for word in wordList:
            for i in range(length):
                intermediate = word[:i] + "*" + word[i+1:]
                wildcards[intermediate].append(word)

        queue = [(beginWord, level+1)]
        visited = {beginWord: True}

        while queue:
            curr, level = queue.pop(0)
            for i in range(length):
                intermediate = curr[:i] + "*" + curr[i+1:]
                for word in wildcards[intermediate]:
                    if word == endWord:
                        return level+1
                    elif not word in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                wildcards[intermediate] = []
        return 0


# @lc code=end
