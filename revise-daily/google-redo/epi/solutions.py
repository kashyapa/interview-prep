def is_palindrome(n):
    div = 1
    while n // div > 10:
        div *= 10

    while n:
        msb = n // div
        lsb = n % 10
        if msb != lsb:
            return False
        n = (n % div) // 10
        div //= 100
    return True


def reverse_digits(n):
    rev = 0
    is_negative = False

    if n < 0:
        is_negative = True
        n *= -1

    while n > 0:
        rem = n % 10
        rev = rev*10 + rem
        n //= 10

    return rev * -1 if is_negative else rev


from collections import namedtuple, defaultdict

def rectangle_intersection(r1, r2):
    Rectangle = namedtuple('Rectangle', ('x', 'y', 'height', 'width'))

    def intersect(r1, r2):

        return r1.x <= r2.x+r2.width and r1.x+r1.width <= r2.x and r1.y <= r2.height + r2.y and r2.y <= r1.y + r1.height

    if intersect(r1, r2):
        return Rectangle(0, 0, -1, -1)
    return Rectangle(
        max(r1.x, r2.x), max(r1.y, r2.y),
        min(r1.x+r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y+r2.height)
    )


def heavy_hitter(stream, k, n):

    table = defaultdict(int)

    for buf in stream:
        table[buf] += 1
        if len(table) == k:
            for p in table:
                table[p] -= 1
                if table[p] == 0:
                    del table[p]

    for buf in table:
        table[buf] = 0

    for buf in stream:
        if buf in table:
            table[buf] += 1

    return [it for it in table.values() if it > n // k  ]

def trapping_water(heights):

    def calculate_volume(list_of_heights):
        volume_collected = 0
        last_seen_highest = list_of_heights[0]
        for i in range(1, len(list_of_heights)):
            if list_of_heights[i] >= last_seen_highest:
                last_seen_highest = max(last_seen_highest, list_of_heights[i])
            else:
                volume_collected += last_seen_highest - list_of_heights[i]
        return volume_collected

    max_h = heights.index(max(heights))
    return calculate_volume(heights[:max_h]) + calculate_volume(list(reversed(heights[max_h+1:])))

from math import inf

def find_maximum_2d_subarray(two_d_subarray):

    def calculate_area_2d_array(arr):

        pillars = []
        max_area = 0

        for i, h in enumerate(arr+[0]):

            while pillars and h < arr[pillars[-1]]:
                height = arr[pillars.pop()]
                width = i - pillars[-1] -1 if pillars else i
                max_area = max(max_area, height*width)
            pillars.append(i)
        return max_area


    table = [0] * len(two_d_subarray[0])
    max_area = -inf
    for row in two_d_subarray:
        table = [x+y if y else 0 for x, y in zip(table, row)]
        max_area = max(max_area, calculate_area_2d_array(table))

    return max_area

def maximum_subarray_sum_circular_subarray(nums):

    def max_sum_subarray(nums):

        local_max = -inf
        global_max = -inf

        for i in range(len(nums)):
            local_max = max(nums[i], local_max+nums[i])
            global_max = max(global_max, local_max)

        return global_max

    def circular_sum_array(nums):

        def compute_running_max_sum(nums):
            partial_sum = nums[0]
            running_sum = [partial_sum]

            for i in range(1, len(nums)):
                partial_sum += nums[i]
                running_sum.append(max(running_sum[-1], nums[i]+ running_sum[-1]))
            return running_sum

        begin_to_end = compute_running_max_sum(nums)
        end_to_start = compute_running_max_sum(nums[::-1])[::-1][1:] + [0]

        return max([begin+end for begin, end in zip(begin_to_end, end_to_start)])
    return max(max_sum_subarray(nums) , circular_sum_array(nums))


class Jug:
    def __init__(self, low, high):
        self.low = low
        self.high = high

def measure_with_defective_jugs(jugs, lower_limit, higher_limit):

    def rec(lower_limit, higher_limit):

        if lower_limit > higher_limit or (lower_limit, higher_limit) in failed_limits:
            return False

        for j in jugs:
            if (lower_limit <= j.low and j.high < higher_limit) or rec(lower_limit - j.low, higher_limit-j.high):
                return True

        failed_limits.add((lower_limit, higher_limit))
        return False

    failed_limits = set()

from heapq import *
from collections import namedtuple
def draw_skyline(buildings_points):
    Rect = namedtuple('Rect', ('left', 'right', 'height'))

    min_left = min([b[0] for b in buildings_points])
    max_right = max([b[1] for b in buildings_points])

    heights = [0] * len(buildings_points)

    for b in buildings_points:
        for i in range(b.left, b.right):
            heights[i-min_left] = max(heights[i-min_left], b.height)

    result = []
    left = 0

    for i in range(1, len(heights)):
        if heights[i] != heights[i-1]:
            result.append(Rect(left+min_left, i+min_left, heights[i-1]))
            left = i
    return result + [Rect(left+min_left, max_right, heights[-1])]

def regular_expression_matching(str, pattern):
    def is_match_here(str, pattern):

        if not pattern:
            return True
        if pattern == "$":
            return not str

        if len(pattern) >= 2:
            if pattern[1] == "*":
                idx = 1
                while idx <= len(str) and pattern[0] in (str[idx-1], "."):
                    if is_match_here(str[idx:], pattern[2:]):
                        return True
                    idx += 1

                return is_match_here(str, pattern[2:])
        return str and pattern[0] in (".", str[0]) and is_match_here(str[1:], pattern[1:])


class Tree:
    def __init__(self,val, left, right):
        self.left = left
        self.right = right
        self.val = val

def merge_two_bst(t1, t2):
    def merge_two_lists(l1, l2):
        pass

    def convert_dll_to_bst(l, n):

        def build_bst_from_dll(start, end):

            mid = start + (end-start)//2
            left_subtree = build_bst_from_dll(start, mid-1)

            cur = head[0]
            head[0] = head[0].next

            cur.left = left_subtree
            cur.right = build_bst_from_dll(mid+1, end)
            return cur
        head = [l]
        return build_bst_from_dll(0, n)


    def get_inorder_nodes(tree, res):
        if not tree:
            return None

        get_inorder_nodes(tree.left, res)
        res.append(tree)
        get_inorder_nodes(tree.right, res)
        return res

    def convert_bst_to_dll(tree):

        res = get_inorder_nodes(tree, [])
        head = res[0]
        prev = head

        for node in res[1:]:
            prev.right = node
            node.left = prev
            prev = node
        return head
    l1 = convert_bst_to_dll(t1)
    l2 = convert_bst_to_dll(t2)

    merged_list = merge_two_lists(l1, l2)

    convert_dll_to_bst(merged_list)


from heapq import *
from collections import deque
def compute_maximum_traffic_in_sliding_window(traffic_info, w):
    max_heap = []
    queue = deque()
    res = [0] * (len(traffic_info) - w)
    for i, traffic in enumerate(traffic_info):
        queue.append(traffic)
        heappush(max_heap, -traffic)

        if len(queue) > w:
            t = queue.popleft()
            if t == -max_heap[0]:
                heappop(max_heap)
            else:
                idx = max_heap.index(t)
                max_heap[idx] = max_heap[-1]
                max_heap.pop()
                heapify(max_heap)
        res[i-w+1] = -max_heap[0]

import math

def sudoku_checker(partial_assignment):
    def has_duplicates(block):
        block = filter(lambda x: x != 0, block)
        return len(list(block)) != len(set(block))

    n = len(partial_assignment)

    for row in partial_assignment:
        if has_duplicates(row):
            return False

    for col in list(zip(*partial_assignment)):
        if has_duplicates(col):
            return False

    block_size = int(math.sqrt(n))
    for block_index_i in range(block_size):
        for block_index_j in range(block_size):
            flattened_list = []
            for i in range(block_index_i * block_size, block_size*(block_index_i+1)):
                for j in range(block_index_j*block_size, block_size*(block_index_j+1)):
                    flattened_list.append(partial_assignment[i][j])
                    if has_duplicates(flattened_list):
                        return False
    return True


def compute_pascal_triangle(n):
    triangle = [[1] * (i+1) for i in range(n)]
    for i in range(len(triangle)):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]


def min_cost_path_triangle(triangle):
    for row in triangle[1:]:
        min_cost_path = [row[i] +
                         min(min_cost_path[max(i-1, 0)], min_cost_path(max(i, len(min_cost_path)-1)))
                         for i in range(len(row))]
