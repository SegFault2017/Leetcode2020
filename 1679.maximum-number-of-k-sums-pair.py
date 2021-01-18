class Solution:
    from collections import Counter

    def maxOperations(self, nums: List[int], k: int) -> int:
        """ Strategy 1: Hash Table

        Args:
            nums (List[int]): a list of integers
            k (int): target value

        Returns:
            int: maximum pairs that sums up to k
        """
        if not nums:
            return 0
        counter = Counter(nums)
        count = 0
        n = len(nums)

        for i in range(n):
            complement = k - nums[i]
            if counter[complement] > 0 and counter[nums[i]] > 0:
                if nums[i] == complement and counter[nums[i]] < 2:
                    continue
                counter[nums[i]] -= 1
                counter[complement] -= 1
                count += 1
        return count
