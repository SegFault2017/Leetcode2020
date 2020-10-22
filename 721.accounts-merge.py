#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
import string


class Disjoint:
    def __init__(self):
        MAX_EMAILS = 10001
        self.rank = range(MAX_EMAILS)
        self.size = [0 for in self.rank]

    def find_rank(self, id: int) -> int:
        """ returns a rank of an unique account

        Args:
            id (int): the id of the account

        Returns:
            int: the rank of the account
        """


class Solution:
    # Union Find
    # Runtime: O(N * M), where N is the number of accounts, M is the # of emails
    # for an account
    ## Space: O(N * M)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # @lc code=end
