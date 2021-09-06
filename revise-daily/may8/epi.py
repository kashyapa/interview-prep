from heapq import *
import math
from collections import deque


class FileSystem:

    def __init__(self):
        self.root = {"/": {}}

    def ls(self, path: str):
        node = self.root
        sub_dirs = path.split("/")
        for d in sub_dirs:
            if d not in node:
                return []
            node = node[d]
        return node.keys()

    def mkDir(self, path: str) -> None:
        node = self.root
        sub_dirs = path.split("/")
        for d in sub_dirs:
            if d not in node:
                node[d] = {}
            node = node[d]

    def add_content_to_file(self, filePath: str, content: str) -> None:
        node = self.root
        sub_dirs = filePath.split("/")
        for d in sub_dirs[:-1]:
            node = node[d]
        node[sub_dirs[-1]] = content

    def read_file_from_path(self, filePath: str) -> str:
        node = self.root
        sub_dirs = filePath.split("/")
        for d in sub_dirs[:-1]:
            node = node[d]
        return node[sub_dirs[-1]]


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


def employeeFreeTime(schedule):
    min_heap = []

    for i, interval in enumerate(schedule):
        heappush(min_heap, (interval, i, 0))
    prev_interval = min_heap[0][0]
    res = []
    prev_interval_end = prev_interval.end
    while min_heap:
        interval, employee, interval_idx = heappop(min_heap)

        if prev_interval_end < interval.start:
            res.append((prev_interval_end, interval.start))
            prev_interval_end = interval.end
        else:
            if prev_interval_end > interval.end:
                prev_interval_end = interval.end
        if len(schedule[employee] > interval_idx + 1):
            heappush(min_heap, (schedule[employee][interval_idx + 1], employee, interval_idx + 1))

    return res


def maxDistance(arrays):

    min_num = arrays[0][0]
    max_num = arrays[0][-1]
    max_diff = math.inf * -1

    for array in arrays[1:]:
        max_diff = max(max_diff, abs(min_num-array[-1]), abs(max_num-arrays[0]))
        max_num = max(array[-1], max_num)
        min_num = min(min_num, array[0])
    return max_diff


# Python program for weighted job scheduling using Dynamic
# Programming and Binary Search

# Class to represent a job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


# A Binary Search based function to find the latest job
# (before current job) that doesn't conflict with current
# job. "index" is index of the current job. This function
# returns -1 if all jobs before index conflict with it.
# The array jobs[] is sorted in increasing order of finish
# time.
def binarySearch(job, start_index):
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start_index - 1

    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1


# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(job):
    # Sort jobs according to finish time
    job = sorted(job, key=lambda j: j.finish)

    # Create an array to store solutions of subproblems. table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]

    table[0] = job[0].profit;

    # Fill entries in table[] using recursive property
    for i in range(1, n):

        # Find profit including the current job
        inclProf = job[i].profit
        l = binarySearch(job, i)
        if (l != -1):
            inclProf += table[l];

        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])

    return table[n - 1]
    #   0
    #  0 1
    # 0 1 2
    #0 1 2 3

def generate_pascal_triangle(n):
    triangle = [[1] * (i+1) for i in range(n)]
    print(triangle[0])
    #print(triangle[1])
    for i in range(1, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        print(triangle[i])

import math

def sudoku_checker(board):
    def rec(i, j):

        if i == len(board):
            j += 1
            if j == len(board[0]):
                return True
            i = 0

        if board[i][j] != 0:
            return rec(i+1, j)

        def check_duplicates(i, j, val):

            if val in board[i]:
                return True

            if val in [board[x][j] for x in range(len(board))]:
                return True

            row_block_size = math.sqrt(len(board))
            col_block_size = math.sqrt(len(board[0]))

            i = i // row_block_size
            j = j // col_block_size

            block_elements = [board[x][y] for x in range((row_block_size) * i, (row_block_size) * (i+1)) for y in range((col_block_size * j), col_block_size * (j+1))]

            if val in block_elements:
                return True

            return False

        for val in range(1, len(board)+1):
            # board[i][j] = val
            if check_duplicates(i, j, val) is not False:
                board[i][j] = val
                if rec(i+1, j):
                    return True
        board[i][j] = 0
        return False

    return rec(0, 0)


def spiral_matrix():
    pass


def print_orders(vertices, edges):

    def explore_all_paths(sources, in_degree, graph, sorted_order):
        if sources:
            for vertex in sources:
                sources_for_next_call = deque(sources)
                sources_for_next_call.remove(vertex)
                sorted_order.append(vertex)
                for child in graph[vertex]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        sources_for_next_call.append(child)

                explore_all_paths(sources_for_next_call, in_degree, graph, sorted_order)
                sorted_order.remove(vertex)

                for child in graph[vertex]:
                    in_degree[child] += 1
        if len(sorted_order) == len(graph):
            print(sorted_order)


    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for parent, child in edges:
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for k, v in in_degree.items():
        if v == 0:
            sources.append(k)

    explore_all_paths(sources, in_degree, graph, [])

    return

class GraphVertex:
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges

def clone_graph():
    pass


from collections import deque
from math import inf
from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:

    def bfs(grid, i, j):
        queue = deque([(i, j)])
        visited = set()
        count = 0
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            count += 1
            for di, dj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (di, dj) not in visited and di < len(grid) and di >= 0 and dj < len(grid[di]) and dj >= 0 and grid[di][dj] == 1:
                    queue.append((di, dj))

        return count

    max_count = 0
    x, y = -1, -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count = bfs(grid, i, j)
                if count > max_count:
                    x, y = i, j

    return max_count


def exist(board: List[List[str]], word: str) -> bool:
    def bfs(i, j):
        queue = deque([(i, j, 0)])
        visited_cells = set()
        while queue:
            i, j, count = queue.popleft()
            if count == len(word) - 1:
                return True

            visited_cells.add((i, j))
            count += 1
            for di, dj in [(i + 1, j), (i, j + 1), (i, j - 1), (i - 1, j)]:
                if (di, dj) not in visited_cells and di >= 0 and di < len(board) and dj >= 0 and dj < len(
                    board[0]) and board[di][dj] == word[count]:
                    queue.append((di, dj, count))
                    if count == len(word) - 1:
                        return True
        return False

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                if bfs(i, j):
                        return True
    return False

if __name__ == "__main__":
    # fs = FileSystem()
    # fs.mkDir("/root/schandra2")
    # fs.add_content_to_file("/root/schandra2/file.txt", "hello world")
    # print(fs.read_file_from_path("/root/schandra2/file.txt"))
    # employeeFreeTime([[Interval([1,2]),Interval([5,6])],
    #                   [Interval([1,3])],
    #                   [Interval([4,10])]
    #                   ])
    #
    # # Driver code to test above function
    # job = [Job(1, 2, 50), Job(3, 5, 20),
    #        Job(6, 19, 100), Job(2, 100, 200)]
    # print("Optimal profit is"),
    # print(schedule(job))

    generate_pascal_triangle(4)
    board = [
        [7, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 0, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
    print(sudoku_checker(board))

    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])

    print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
                          ))
    print(exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))