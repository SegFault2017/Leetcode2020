
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     """ Strategy 2: 2 pointers
    #     Runtime: O(n * log(n)), where n is the size of nums
    #     Space: O(n)

    #     Args:
    #         nums (List[int]): list of integers
    #         target (int): target value

    #     Returns:
    #         List[int]: [i,j], where i != j, 0 <= i,j<=n
    #     """

    #     # stores (val, idx) as a tuple
    #     temp = [(val, idx) for idx, val in enumerate(nums)]
    #     temp.sort(key=lambda x: x[0])

    #     n = len(nums)
    #     # 2 pointers
    #     i, j = 0, n-1

    #     while i < j:
    #         if temp[i][0] + temp[j][0] == target:
    #             return (temp[i][1], temp[j][1])
    #         elif temp[i][0] + temp[j][0] > target:
    #             j -= 1
    #         else:
    #             i += 1

    #     return [-1, -1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Strategy 3: Hash Table
        Runtime:O(n)
        Space:O(n)

        Args:
            nums (List[int]):  list of integers
            target (int): target value

        Returns:
            List[int]: [i,j], where i != j, 0 <= i,j<=n
        """

        # hash table, key = x, value = idx
        cache = {}

        for idx, x in enumerate(nums):
            complement = target - x
            if complement in cache:
                return (cache[complement], idx)
            cache[x] = idx

        return [-1, -1]
        # @lc code=end
