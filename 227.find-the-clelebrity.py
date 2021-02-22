# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def isCelebrity(self, _id: int, n: int) -> int:
        for i in range(n):
            if i == _id:
                continue
            if knows(_id, i) or not knows(i, _id):
                return False
        return True

    def findCelebrity(self, n: int) -> int:
        """ Strategy 1: Logical Deduction
        Runtime: O(n)
        Space: O(1)


        Args:
            n (int): n people

        Returns:
            int: return the celetbrity if exist, otherwise -1
        """
        candidate = 0

        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        return candidate if self.isCelebrity(candidate, n) else -1
