
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Hashmap
        Runtime: O(n), where n is the size of nums
        Space: O(1)

        Args:
            nums (List[int]): a list of integers
            target (int): the target value

        Returns:
            List[int]: pair of indices that has value add up to target
        """
        cache = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in cache:
                return [cache[complement], i]
            cache[nums[i]] = i
        return []
# @lc code=end
