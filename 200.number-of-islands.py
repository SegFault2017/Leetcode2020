#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Disjoint:
    def __init__(self, grid:List[List[int]]):
        LAND = "1"
        self.n = len(grid)
        self.m = len(grid[0])
        self.islands = 0
        
        self.size =[]
        self.rank = [] # a list of tuples, and a tuple contians [y,x]

        for y in range(self.n):
            for x in range(self.m):
                if grid[y][x] == LAND:
                    self.islands += 1
                    self.size.append(1)
                    self.rank.append(y * self.m + x)
                else:
                    self.size.append(0)
                    self.rank.append(-1)
    
    def weighted_union(self, cell:int, other:int) -> None:
        cell_root = self.find_rank(cell)
        other_root = self.find_rank(other)

        if self.size[cell_root] < self.size[other_root]:
            self.rank[cell_root] = self.rank[other_root]
            self.size[other_root] += self.size[cell_root]
        else:
            self.rank[other_root] = self.rank[cell_root]
            self.size[cell_root] += self.size[other_root]
        self.islands -=1
        return None

    ##find root of cell
    def find_rank(self, cell:tuple) -> int:
        y,x = cell
        while True:
            root = self.m * y + x
            if self.rank[root] == root:
                return root
        

    ## Detemrine wherether cell and other have the same connectivity,
    def find(self, cell:tuple, other:tuple) -> bool:
        return self.find_rank(cell) == self.find_rank(other)
        
        

class Solution:
    #Union Find
    def numIslands(self, grid: List[List[str]]) -> int:
        disjoint = Disjoint(grid)
        LAND = "1"
        n = len(grid)
        m = len(grid[0])

        def valid(y:int, x:int) -> tuple:
            for r,c in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                if 0<= r < self.n and 0<= c < self.m:
                    yield (r,c)
            return ()
        
        for y in range(n):
            for x in range(m):
                if grid[y][x] == LAND:
                    for diry,dirx in valid(y,x):
                        disjoint.weighted_union((y,x),(diry,dirx))
                    
                    
        
        
        
        return disjoint.islands

        









    #DFS
    # def numIslands(self, grid: List[List[str]]) -> int:
        # n = len(grid)
        # m = len(grid[0])
        # LAND = "1"
        # WATER = "0"

        # def valid(y:int, x:int) -> tuple:
        #     for r,c in [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]:
        #         if 0<= r < n and 0<= c < m:
        #             yield(r,c)
        #     return ()
        
        # def BFS(y:int ,x:int) -> int:
        #     grid[y][x] = WATER
        #     queue = [(y,x)]
            
        #     while queue:
        #         y, x = queue.pop()
        #         for r,c in valid(y,x):
        #             if grid[r][c] == LAND:
        #                 queue.append((r,c))
        #                 # print(queue,grid[r][c] != 0,(r,c))
        #                 grid[r][c] = WATER
                        
        #     return 1

        # islands = 0
        # for y in range(n):
        #     for x in range(m):
        #         if grid[y][x] == LAND:
        #             islands += BFS(y,x)
        # return islands



        

# @lc code=end
