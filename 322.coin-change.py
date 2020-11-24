#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Strategy 1: Dynamic Programming
        Runtime: O(n * mount + 1), where n is the length of the coins 
        Space: O(n)


        Args:
            coins (List[int]): list of coins
            amount (int): The amount value

        Returns:
            int: Minimum # of coins that make up the amt.
        """
        dp = [amount + 1 for i in range(amount+1)]
        dp[0] = 0
        n = len(coins)

        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        # print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1


# @lc code=end
