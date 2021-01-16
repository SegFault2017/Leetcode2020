class SuffixTrie:

    def __init__(self, string):
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_trie_from(string)

    def insert(self, i, string):
        curr = self.root
        for j in range(i, len(string)):
            if string[j] not in curr:
                curr[string[j]] = {}
            curr = curr[string[j]]
        curr[self.end_symbol] = True

    def populate_suffix_trie_from(self, string):
        for i in range(len(string)):
            self.insert(i, string)
        return

    def contains(self, string):
        curr = self.root
        for c in string:
            curr = curr[c]
        return self.end_symbol in curr


st = SuffixTrie("babc")
contains = st.contains("bc")
print("Restlt: ", contains)
