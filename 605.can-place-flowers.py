#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Strategy 1: Linear scan 

        Args:
            flowerbed (List[int]): a list of int, 0 means empty pot and 1 means occupies
            n (int): number of plants to plant

        Returns:
            bool: whether is possible to plant all plants
        """

        size = len(flowerbed)
        EMPTY = i = 0
        while i < size and n > 0:
            if (flowerbed[i] == EMPTY and (i == 0 or flowerbed[i-1] == EMPTY) and (i == size-1 or flowerbed[i+1] == EMPTY)):
                flowerbed[i] = 1
                n -= 1
                # print(n, flowerbed)
            i += 1
        return n <= 0

# @lc code=end
