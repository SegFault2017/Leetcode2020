#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """ Linear scan
        Runtime: O(n)
        Space:O(1)

        Args:
            nums (List[int]): lists of 0's and 1's
            k (int): distanct inbetween 1's

        Returns:
            bool: determine whethere all 1's are sepeareted by at k spaces
        """

        count = k

        for num in nums:
            if num == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        return True

# @lc code=end
