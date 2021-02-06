#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """ Strategy: Stack 
        Runtime:O(n), where n is the size of nums
        Space:O(n)

        Args:
            nums (List[int]): list of integers      

        Returns:
            List[int]: 
        """
        n = len(nums)
        if n == 0:
            return []

        output = [0] * n
        stack = []

        for i in range(2 * n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()

            output[i % n] = nums[stack[-1]] if stack else -1
            stack.append(i % n)
        return output


# @lc code=end
