class Solution(object):
    def grouping_options(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        row_end = n
        col_end = k
        dp_list = [[0] * (col_end + 1) for _ in range(row_end + 1)]
        dp_list[0][0] = 1
        res = 0

        for i in range(1, row_end + 1):
            for j in range(1, min(col_end, i) + 1):
                dp_list[i][j] = dp_list[i - j][j] + dp_list[i - 1][j - 1]

        return dp_list[-1][-1]


def main():
    n = 4
    k = 3
    solution = Solution()
    res = solution.grouping_options(n, k)
    print(res)


if __name__ == "__main__":
    main()
