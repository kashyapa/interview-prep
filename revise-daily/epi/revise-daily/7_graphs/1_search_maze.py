from collections import namedtuple

Coordinate = namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze):
    def search_maze_helper(c):
        if 0 > c.x >= len(maze) or 0 > c.y >= len(maze[0]):
            return False

        if c.x == len(maze) - 1 and c.y == len(maze[0]) - 1:
            return True

        if c in failed_points or c in path:
            return False

        path.append(c)
        if any(
            map(search_maze_helper(
                map(Coordinate, (c.x+1, c.x-1, c.x, c.x),
                                (c.y, c.y, c.y+1, c.y-1)
                    )
            ))
        ):
            return True
        del path[-1]
        failed_points.add(c)
        return False

    path = []
    failed_points = set()

    return search_maze_helper(Coordinate(0, 0))


if __name__ == '__main__':
    search_maze([[]])
