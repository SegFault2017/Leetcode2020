class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """ Strategy 1: 2 Pointers

        Args:
            nums (List[int]): a list of int
            x (int): the target value

        Returns:
            int: the minimum # of operations to reduce x to 0
        """
        total = sum(nums)
        n = len(nums)
        left = 0
        curr = 0
        longest = -1

        for right in range(n):
            curr += nums[right]
            while curr > total-x and left <= right:
                curr -= nums[left]
                left += 1
            if curr == total - x:
                longest = max(longest, right - left + 1)
        return n - longest if longest != -1 else -1
