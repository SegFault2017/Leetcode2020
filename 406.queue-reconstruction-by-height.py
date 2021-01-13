#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """ Strategy 1: Greedy
        Runtime: O(n), where n is the # of people
        Space: O(n)

        Args:
            people (List[List[int]]): a list of [hi,ki], where hi is the height of the ith person, 
            ki is the # of peopel has height >= to the ith person.

        Returns:
            List[List[int]]: the reconstructued queue foolows the rules, [hi,ki]
        """

        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
        # @lc code=end
