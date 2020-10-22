from os import set_blocking
from typing import List


class Disjoint:
    def __init__(self, grid: List[List[str]]) -> None:
        self.n = len(grid)
        self.m = len(grid[0])
        LAND = 1

        self.rank = []
        self.size = []
        self.islands = 0

        for y in range(self.n):
            for x in range(self.m):
                if grid[y][x] == LAND:
                    self.islands += 1
                    self.rank.append(self.m * y + x)
                    self.size.append(1)
                else:
                    self.rank.append(-1)
                    self.size.append(0)

    def find_rank(self, cell: tuple) -> int:
        y, x = cell
        parent_i = self.m * y + x
        while self.rank[parent_i] != parent_i:
            parent_i = self.rank[parent_i]
        return parent_i

    def find(self, cell: tuple, other: tuple) -> bool:
        return self.find_rank(cell) == self.find_rank(other)

    def weighted_union(self, cell: tuple, other: tuple) -> None:
        cell_root = self.find_rank(cell)
        other_root = self.find_rank(other)
        if cell_root == other_root:
            return
        if self.size[cell_root] < self.size[other_root]:
            self.rank[cell_root] = self.rank[other_root]
            self.size[other_root] += self.size[cell_root]
        else:
            self.rank[other_root] = self.rank[cell_root]
            self.size[cell_root] += self.size[other_root]
        self.islands -= 1
        return


def main():
    grid = [[1, 0, 0, 1],  # 0, 0 -> 3, 1 -> 2, 2 -> 1, 2 -> 3, 3 -> 0, 3 -> 27
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]]
    disjoint = Disjoint(grid)

    n = len(grid)
    m = len(grid[0])
    LAND = 1
    WATER = 0

    def valid(y: int, x: int) -> tuple:
        for r, c in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if 0 <= r < n and 0 <= c < m and grid[r][c] == LAND:
                yield (r, c)
        return (-1, -1)

    for y in range(n):
        for x in range(m):
            if grid[y][x] == LAND:
                grid[y][x] = WATER
                for dir_y, dir_x in valid(y, x):
                    disjoint.weighted_union((y, x), (dir_y, dir_x))

    print(disjoint.islands)

    return


if __name__ == "__main__":
    main()
    pass
