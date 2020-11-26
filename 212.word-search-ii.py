#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

from typing import List
# @lc code=start

from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.is_word = False
        self.word = ""
        self.children = defaultdict(Node)

    def isWord(self):
        return self.is_word

    def getChild(self, char: str) -> 'Node':
        return self.children.get(char)

    def getWord(self):
        return self.word

    def setWord(self, word: str):
        self.is_word = True
        self.word = word


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.setWord(word)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """Strategy 1: Backtracking + Trie
        Runtime: O(4* l), where l is the longest word in words
        Space: O(w), where w is total character length of words in words list

        Args:
            board (List[List[str]]): 2-D list representing the board
            words (List[str]): a list of string to search on the board

        Returns:
            List[str]: words that are founded on board
        """

        n = len(board)
        m = len(board[0])
        output = set()
        trie = Trie()

        for word in words:
            trie.insert(word)

        def valid(y: int, x: int) -> tuple:
            for row, col in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= row < n and 0 <= col < m:
                    yield (row, col)
            return ()

        def dfs(y: int, x: int, currNode: Node) -> None:
            currNode = currNode.getChild(board[y][x])
            if not currNode:
                return

            if currNode.isWord():
                output.add(currNode.getWord())

            temp = board[y][x]
            board[y][x] = "#"
            for row, col in valid(y, x):
                if board[row][col] != "#":
                    dfs(row, col, currNode)
            board[y][x] = temp
            return

        for y in range(n):
            for x in range(m):
                if len(output) == len(words):
                    return list(output)
                dfs(y, x, trie.root)
        return list(output)
        # @lc code=end
