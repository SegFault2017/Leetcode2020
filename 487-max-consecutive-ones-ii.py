class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """ Strategey 1: Sliding Window
        Runtime: O(n), where n is the size of nums
        Space: O(1)


        Args:
            nums (List[int]): list of binary numbers

        Returns:
            int: the maximum number of consecutive ones in the array if you can
             flip at most one zero.
        """
        n = len(nums)
        l = r = 0
        longest = 0
        zeros = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1

            while zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1
        return longest
