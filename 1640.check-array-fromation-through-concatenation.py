class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """Strategy 1: Hash
        Runtime: O(n), where n is the number of elements in the arr
        Space:o(n)


        Args:
            arr (List[int]): a list of integers
            pieces (List[List[int]]): list of pieces,

        Returns:
            bool: determine wherther pieces can form the array arr.
        """
        cache = {x[0]: x for x in pieces}
        n = len(arr)
        i = 0

        while i < n:
            if arr[i] not in cache:
                return False
            piece = cache[arr[i]]
            for x in piece:
                if x != arr[i]:
                    return False
                i += 1

        return True
