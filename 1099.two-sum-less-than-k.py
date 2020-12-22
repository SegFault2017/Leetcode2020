class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """Strategy: 2 Pointers
        Runtime: O(n log n)
        Space: O(n log n)
        Args:
            nums (List[int]): a list of integers
            k (int): the target value k

        Returns:
            int: max sum of nums[i] + nums[j] < k
        """
        n = len(nums)
        i, j = 0, len(nums) - 1
        nums.sort()
        max_sum = -1

        while i < j:
            added = nums[i] + nums[j]
            if added < k:
                max_sum = max(max_sum, added)
                i += 1
            else:
                j -= 1
        return max_sum
