#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """Strategy 1: Dynamic Programming
        Runtime: O(n ^ amount + 1), where n is the lengn of coin list
        Space: O(n * amount + 1)

        Args:
            amount (int): The target amount
            coins (List[int]): list of denominations

        Returns:
            int: The number of combinations to make up the given amt.
        """
        n = len(coins)
        dp = [[1 if x == 0 else 0 for x in range(
            amount+1)] for y in range(n+1)]

        for x in range(1, amount+1):
            for y in range(1, n+1):
                if coins[y-1] <= x:
                    dp[y][x] = dp[y-1][x] + dp[y][x - coins[y-1]]
                else:
                    dp[y][x] = dp[y-1][x]
        # print()
        for row in dp:
            print(row)
        return dp[n][amount]
# @lc code=end
