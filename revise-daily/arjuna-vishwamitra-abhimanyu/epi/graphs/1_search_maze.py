def search_maze(maze):
    def rec(x, y):

        if x == len(maze) and y == len(maze[0]):
            return True
        elif x >= len(maze)-1 or y >= len(maze[0]) or x < 0  or y < 0 or maze[x][y] == "1"\
            or (x, y) in (visited, failed_points):
            return False

        for i, j in [(x+1,y), (x-1,y), (x, y+1), (x, y-1)]:
            if rec(i, j):
                return True
        failed_points.add((x, y))
        return False

    visited = set()
    failed_points = set()
    