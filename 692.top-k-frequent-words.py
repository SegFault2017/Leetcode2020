#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Element:
    def __init__(self, word:str,freq:int):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other) -> bool:
        return self.freq < other.freq or (self.freq == other.freq and self.word < other.word)
     

    
    def __repr__(self):
        return "(" + self.word + ", " + str(self.freq) + ")"
        
class Solution:
    from collections import Counter
    import random
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []
        
        counter = Counter(words)
        unique = []

        for key in counter:
            unique.append(Element(key, counter[key]))

        def partition(start:int, end:int, pivot_i:int) -> int:
            # unique[pivot_i], unique[end] = unique[end], unique[pivot_i]
            pivot = unique[end]
            i = start
            
            for j in range(start,end):
                if unique[j] < pivot:
                    unique[i], unique[j] = unique[j], unique[i]
                    i = i + 1
            unique[i], unique[end] = unique[end], unique[i]
            return i

        def quickSelect(start:int, end:int, k:int) -> None:
            if start >= end:
                return
            
            pivot_i = random.randint(start, end)
            index = partition(start, end, pivot_i)
            
            if k == index:
                return
            elif k < index:
                quickSelect(start, index-1,k)
            else:
                quickSelect(index+1, end, k)
        n = len(unique)
        quickSelect(0, n - 1, n-k)
        print(unique)
        # print(sorted(unique[n-k:], key=lambda x: (x.freq, x.word)))
        return [unique[i].word for i in range(n-k,n)]

   
        
# @lc code=end

