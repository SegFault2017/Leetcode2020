#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ Strategy 1:2 Pointers
        Runtime:O(n), where n is the size of numbers
        Space:O(1)

        Args:
            numbers (List[int]): [description]
            target (int): [description]

        Returns:
            List[int]: [description]
        """
        i, j = 0, len(numbers) - 1

        while i < j:
            added = numbers[i] + numbers[j]
            if added == target:
                return [i+1, j+1]
            elif added < target:
                i += 1
            else:
                j -= 1
        return []
 # @lc code=end
