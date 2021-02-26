from collections import deque

"""
    Get  current coordinate from queue
    get the neighbors of that coordinate
    if any of the neighbors is white, flip it
    Add the flipped coordinate to the queue
"""


def flip_boolean_matrix(x, y, image):
    color = image[x][y]
    q = deque([(x, y)])
    image[x][y] = not image[x][y]

    while q:
        x, y = q.popleft()
        for x1, y1, in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
            if 0 <= x1 < len(image) and 0 <= y1 < len(image[x1]) and image[x1][y1] == color:
                image[x1][y1] = not image[x1][y1]
                q.append((x1, y1))


if __name__ == '__main__':
    flip_boolean_matrix(2, 3, [[]])

