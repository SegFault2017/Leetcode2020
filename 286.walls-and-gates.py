class Solution:
    from collections import Counter

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Strategy 1: BFS
        Runtime: O(n * m), where m is the # of columns and n is the # of rows
        Space: O(m * n)
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        n = len(rooms)
        m = len(rooms[0])
        Q = []
        GATE = 0
        INF = 2147483647
        WALL = -1

        def valid(y: int, x: int) -> tuple:
            for r, c in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= r < n and 0 <= c < m and rooms[r][c] == INF:
                    yield (r, c)
            return ()

        def bfs() -> None:
            while Q:
                y, x, depth = Q.pop(0)
                for r, c in valid(y, x):
                    rooms[r][c] = depth + 1
                    Q.append((r, c, depth+1))
            return

        for y in range(n):
            for x in range(m):
                if rooms[y][x] == GATE:
                    Q.append((y, x, 0))

        bfs()
        return
