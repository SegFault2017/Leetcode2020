class ValidWordAbbr:
    from collections import defaultdict

    def __init__(self, dictionary: List[str]):
        """Stretegy: Set + Hash
        Rutime:O(n), where n is the size of the ictionary
        Space:O(n)

        Args:
            dictionary (List[str]): the dictionary
        """
        self.abbrDict = defaultdict(set)
        print(self.abbrDict)
        for word in dictionary:
            abbr = self.toAbbr(word)
            words = self.abbrDict[abbr] if abbr in self.abbrDict else set()
            words.add(word)
            self.abbrDict[abbr] = words
        return

    def toAbbr(self, word: str) -> str:
        n = len(word)
        if n <= 2:
            return word
        return word[0] + str(n-2) + word[n-1]

    def isUnique(self, word: str) -> bool:
        abbr = self.toAbbr(word)
        words = self.abbrDict.get(abbr)
        return not words or (len(words) == 1 and word in words)


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
