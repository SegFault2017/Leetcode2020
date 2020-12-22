class TwoSum:
    """Strategy 1: Hash
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        return

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        Runtime: O(1)
        Space:O(1)
        """
        self.nums.append(number)
        return

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        Runtime: O(n)
        Space:O(n)
        """
        cache = set()
        for x in self.nums:
            complement = value - x
            if complement in cache:
                return True
            cache.add(x)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
