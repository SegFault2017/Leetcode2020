# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        Strategy 1: DFS
        Runtime:O(n * m), where n is the height of the room, and m is the width of the room
        Space: O(n * m)
        :type robot: Robot
        :rtype: None
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        N = len(directions)
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(cell=(0, 0), d=0) -> None:
            visited.add(cell)
            robot.clean()

            for i in range(N):
                new_d = (d + i) % N
                new_cell = (cell[0] + directions[new_d][0],
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    dfs(new_cell, new_d)
                    go_back()
                robot.turnRight()
            return
        dfs()
