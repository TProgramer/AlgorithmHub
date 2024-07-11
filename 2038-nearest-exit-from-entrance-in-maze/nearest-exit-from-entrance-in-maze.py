from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        # size of maze
        maze_row = len(maze)
        maze_col = len(maze[0])

        # use BFS to count steps for exit
        queue = deque([(entrance, 1)])
        maze[entrance[0]][entrance[1]] = 'v'

        # val for 4 direction of movement
        dirY = [-1, 1, 0, 0]
        dirX = [0, 0, -1, 1]

        while queue:
            
            location, depth = queue.popleft()
            nowY, nowX = location[0], location[1]
            print(nowY, nowX, depth)
            # search 4 ways to move
            for direc in range(4):
                newY, newX = nowY + dirY[direc], nowX + dirX[direc]

                # check new way is possible to move
                # use 'v' to show it's visited
                if 0 <= newY < maze_row and 0 <= newX < maze_col and maze[newY][newX] == '.':

                    # check if it's exit
                    if newY == 0 or newY == maze_row - 1 or newX == 0 or newX == maze_col - 1:
                        print(newY, newX)
                        return depth

                    maze[newY][newX] = 'v'
                    queue.append(((newY, newX), depth + 1))
        
        # if not found exit, return -1
        return -1