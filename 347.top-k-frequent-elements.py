#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    #pivot 7
    #[11,3,9,6,12,7]
    #[3,,9,6,11,7]
    #
    from collections import Counter
    import random
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        counter = Counter(nums)
        unique = list(counter.keys())
        
        def partition(start:int, end:int, pivot_i: int) -> int:
            unique[pivot_i], unique[end] = unique[end], unique[pivot_i]
            pivot = counter[unique[end]]
            i = start

            for j in range(start, end):
                if counter[unique[j]] < pivot:
                    unique[i], unique[j] = unique[j], unique[i]
                    i +=1
                
            unique[i], unique[end] = unique[end], unique[i]
            return i
        
        def quickSelect(start:int, end:int, k:int) -> None:
            if start == end:
                return []
            
            pivot_i = random.randint(start,end)
            index = partition(start, end, pivot_i)
            
            if k == index:
                return
            elif k < index:
                quickSelect(start, index-1,k)
            else:
                quickSelect(index+1,end, k)
    
            return
        n = len(unique)    
        quickSelect(0,n-1,n-k)
        print(unique)
        return unique[n-k:]
       

# @lc code=end
