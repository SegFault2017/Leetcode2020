#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     """ Strategy 1: BFS
    #     Runtime: O(n * m ^2), where n is the number of words, m is the length of a word
    #     Space: O(n * m ^2)

    #     Args:
    #         beginWord (str): the word to begin with
    #         endWord (str): the destination word
    #         wordList (List[str]): list of words

    #     Returns:
    #         int: # of transformations
    #     """
    #     # bases cases
    #     if not endWord or not beginWord or len(beginWord) != len(endWord) \
    #             or endWord not in wordList or not wordList:
    #         return 0
    #     length = len(beginWord)
    #     wildcards = defaultdict(list)
    #     level = 0

    #     for word in wordList:
    #         for i in range(length):
    #             intermediate = word[:i] + "*" + word[i+1:]
    #             wildcards[intermediate].append(word)

    #     queue = [(beginWord, level+1)]
    #     visited = {beginWord: True}

    #     while queue:
    #         curr, level = queue.pop(0)
    #         for i in range(length):
    #             intermediate = curr[:i] + "*" + curr[i+1:]
    #             for word in wildcards[intermediate]:
    #                 if word == endWord:
    #                     return level+1
    #                 elif not word in visited:
    #                     visited[word] = True
    #                     queue.append((word, level+1))
    #             wildcards[intermediate] = []
    #     return 0

    def __init__(self) -> None:
        self.length = 0
        self.wildcards = defaultdict(list)
        pass

    def findTransform(self, q: List[tuple], visited: dict, o_visited: dict) -> int:
        curr, level = q.pop(0)
        for i in range(self.length):
            intermediate = curr[:i] + "*" + curr[i+1:]
            for word in self.wildcards[intermediate]:
                if word in o_visited:
                    return level + o_visited[word]
                if word not in visited:
                    visited[word] = level+1
                    q.append((word, level+1))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ Strategy 1: Bidirectional
        Runtime: O(n * m ^2), where n is the number of words, m is the length of a word
        Space: O(n * m ^2)

        Args:
            beginWord (str): the word to begin with
            endWord (str): the destination word
            wordList (List[str]): list of words

        Returns:
            int: # of transformations
        """

        if not endWord or not beginWord or len(beginWord) != len(endWord) \
                or endWord not in wordList or not wordList:
            return 0

        self.length = len(beginWord)
        q_begin = [(beginWord, 1)]
        q_end = [(endWord, 1)]
        v_begin = {beginWord: True}
        v_end = {endWord: True}

        for word in wordList:
            for i in range(self.length):
                intermediate = word[:i] + "*" + word[i+1:]
                self.wildcards[intermediate].append(word)

        while q_begin and q_end:
            found = self.findTransform(q_begin, v_begin, v_end)
            if found:
                return found
            found = self.findTransform(q_end, v_end, v_begin)
            if found:
                return found
        return 0


# @lc code=end
