from heapq import *


class Interval:
    def __init__(self, interval):
        self.start = interval[0]
        self.end = interval[1]

    def __lt__(self, other):
        return other.end > self.end



def minMeetingRooms(intervals) -> int:
    min_heap = []
    intervals.sort(key=lambda x: x[0])
    max_meetings = 0

    for i in range(len(intervals)):
        # keep pushing meeting intervals until the next earliest end time of a meeting
        while min_heap and min_heap[0].end <= intervals[i][0]:
            heappop(min_heap)

        heappush(min_heap, (Interval(intervals[i])))
        max_meetings = max(max_meetings, len(min_heap))

    return max(max_meetings, len(min_heap))

from collections import deque

def minKnightMoves(self, x: int, y: int) -> int:
    queue = deque([(0, 0, 0)])
    x, y, visited = abs(x), abs(y), set([(0, 0)])
    while queue:
        i, j, steps = queue.popleft()

        if (i, j) == (abs(x), abs(y)):
            return steps

        for p, q in [(i - 2, j + 1), (i - 1, j + 2),
                     (i + 2, j - 1), (i + 2, j + 1), (i + 1, j - 2), (i + 1, j + 2)]:
            if (p, q) not in visited and -1 <= p <= x + 2 and -1 <= q <= y + 2:
                visited.add((p, q))
                queue.append((p, q, steps + 1))

    return -1


class EmployeeInterval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start > other.start


def employee_free_time(schedule):

    # employees intervals are sorted according to start time
    # place employee intervals in heap
    # while placing , check if the start time is grater than the greatest end time of the intervals in the heap

    min_heap = []
    for i in range(len(schedule)):
        heappush(min_heap, (EmployeeInterval(schedule[i][0], schedule[i][1]),  i, 0))

    previous_interval = min_heap[0].end
    res = []
    while min_heap:
        cur_interval, row_index, col_index = heappop(min_heap)
        if cur_interval.start > previous_interval.end:
            res.append((previous_interval.end, cur_interval.start))
            previous_interval = cur_interval
        else:
            if cur_interval.end > previous_interval.end:
                previous_interval = cur_interval

        if col_index + 1 < len(schedule[row_index]):
            heappush(min_heap, (EmployeeInterval(schedule[row_index][col_index+1]),
                                row_index, col_index+1))
    return res

class GraphVertex:

    def __init__(self, v, edges):
        self.v = v
        self.edges = []

from collections import defaultdict


def find_order(words):

    graph = {} #defaultdict(list)
    in_degree = {} # defaultdict(int)

    for word in words:
        for c in word:
            graph[c] = []
            in_degree[c] = 0

    for i in range(0, len(words)-1):
        w1, w2 = words[i], words[i+1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                graph[w1[j]].append(w2[j])
                in_degree[w2[j]] += 1
                break

    sources = deque()
    for k, v in in_degree.items():
        if v == 0:
            sources.append(k)

    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        for q in graph[vertex]:
            in_degree[q] -= 1
            if in_degree[q] == 0:
                sources.append(q)
    return ''.join(sorted_order)


class TicTacToe:
    def __init__(self, n):
        self.row = [0] * n
        self.col = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def tic_tac_toe(self, row_index, col_index, player):
        self.row[row_index] += 1 if player == 1 else -1
        self.col[col_index] += 1 if player == 1 else -1

        if row_index+col_index == 2:
            self.diag1 += 1 if player == 1 else -1
        if row_index - col_index == 0:
            self.diag2 += 1 if player == 1 else -1

        if abs(self.row[row_index]) == self.n or abs(self.col[col_index]) == self.n \
            or abs(self.diag1) == self.n or self.diag2 == abs(self.n):
            return 1 if player == 1 else 2

#
# Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.
#
# Implement the WordDistance class:
#
# WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

class WordDistance:
    def __init__(self, words):
        self.count = defaultdict(list)
        for i, w in enumerate(words):
            self.count[w].append(i)

    def shortest_distance(self, w1, w2):
        l1 = self.count[w1]
        l2 = self.count[w2]
        import math
        i , j = 0, 0
        min_dist = math.inf
        while i < len(w1) and j < len(w2):
            min_dist = min(min_dist, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return min_dist


class AutocompleteSystem:


    def insert_suffix(self, i, str):
        node = self.root

        for c in str:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.end_symbol] = str



    def __init__(self, sentences, times):
        self.root = {}
        self.rank = 0
        self.end_symbol = "*"
        self.keyword = ""

        for sentence in sentences:
            for i in range(len(sentence)):
                self.insert_suffix(i, sentence[i:])


    def dfs(self, node):
        ret = []
        if not node[self.end_symbol]:
            ret.append(node[self.end_symbol])
        for key in node:
            ret.extend(self.dfs(node[key]))
        return ret

    def search(self, str):
        node = self.root
        res = []
        for c in str:
            if c not in node:
                return []
            node = node[c]
        return self.dfs(node)

    def input(self, c):
        node = self.root

        if c != self.end_symbol:
            self.keyword += c
            return self.search(self.keyword)


def minimum_removal_for_valid_parentheses(s):

    l = list(s)
    stack = []
    res = [""] * len(s)

    for i in range(len(l)):
        if l[i] not in ("(", ")"):
            res[i] = l[i]
        elif l[i] == "(":
            stack.append(i)
        else:
            if stack:
                res[i] = l[i]
                res[stack.pop()] = "("

    return ''.join(res)

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
def subarraySum(nums, K):
    running_sum = 0
    map = {0: 1}

    count = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        if running_sum - K in map:
            count += map.get(running_sum - K) + 1
        map[running_sum] = map.get(running_sum, 0) + 1

    return count

# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

def subarraysDivByK(A, k) -> int:
    map = {0: 1}
    sum = 0
    count = 0
    for i in range(len(A)):
        sum += A[i]
        sum %= k
        if sum < 0:
            sum += k
        if sum in map:
            count += map.get(sum, 0)
        map[sum] = map.get(sum, 0) + 1
    return count

#Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

def checkSubarraySum(self, nums, k: int):
    map = {0: -1}
    running_sum = 0
    for i in range(len(nums)):
        running_sum += nums[i]
        if k != 0:
            running_sum = running_sum % k

        if running_sum in map:
            if i - map[running_sum] > 1:
                return True
        else:
            map[running_sum % k] = i
    return False

# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.

def pivot_index(nums):

    S = sum(nums)
    prefix_sum  = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum == S - prefix_sum:
            return i
    return  -1


def serialize_binary_tree(root, res):

    if not root:
        res.append("None")
        return res
    res.append(str(root.val) + ",")

    res = serialize_binary_tree(root.left, res)
    res = serialize_binary_tree(root.right, res)

    return res

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def deserialize_binary_tree(l):

    if l[0] == "None":
        l.pop(0)
        return None

    root = TreeNode(l[0])
    l.pop(0)
    root.left = deserialize_binary_tree(l)
    root.right = deserialize_binary_tree(l)
    return root


# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
# connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any path.
class MaxSum:
    max_sum = None
    def __init__(self):
        MaxSum.max_sum = 0


def binary_tree_max_sum(root):

    def rec(root):

        if not root:
            return 0

        lc = rec(root.left)
        rc = rec(root.right)
        local_sum  = max(lc+root.val, rc+root.val)

        local_sum = max(local_sum, root.val)
        MaxSum.max_sum = max(MaxSum.max_sum, local_sum)
        MaxSum.max_sum = max(MaxSum.max_sum, lc+rc+root.val)
        return local_sum

    rec(root)
    return MaxSum.max_sum

import math

def trapping_rain_water(heights):

    def compute_water_volume(wall_heights):

        water_volume = 0
        max_height_seen = math.inf
        for i, h in enumerate(wall_heights):
            max_height_seen = max(max_height_seen, h)
            water_volume += max_height_seen - h

        return water_volume

    max_height_index = heights.index(max(heights))

    return compute_water_volume(heights[:max_height_index]) + \
           compute_water_volume(reversed(heights[max_height_index+1]))


def product_array(nums):
    p = 1
    res = []
    for i in range(len(nums)):
        res.append(p)
        p = p * nums[i]

    p = 1
    for i in reversed(range(len(nums)-1)):
        res[i] = res[i] * p
        p = p * nums[i]
    return res

from collections import namedtuple

LcaResult = namedtuple('LcaResult', ('target_nodes', 'ancestor_node'))

def lca(root, p, q):


    if not root:
        return None

    left_result = lca(root.left, p, q)

    if left_result.target_nodes == 2:
        return left_result

    right_result = lca(root.right, p, q)
    if right_result.target_nodes == 2:
        return right_result

    target_nodes = left_result.target_nodes + right_result.target_nodes + 1 if root.val in (p, q) else 0

    cur_result = LcaResult(target_nodes, root if target_nodes == 2 else None)
    return cur_result


def word_breakII(str, words):
    word_count = {}
    for i, word in enumerate(words):
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

    dp = [0] * len(str)

    for i in range(len(str)):

        substr = str[:i+1]
        if substr in word_count:
            dp[i] = i+1
            print(substr)
            continue

        for j in range(i):
            if dp[j] != 0 and str[j+1:i+1] in word_count:
                dp[i] = i-j
                print(str[j:i+1])
    print(dp)
    i = len(str)-1
    res = []
    if dp[-1] > 0:
        while i >= 0:
            res.append(str[i-dp[i]: i])
            i = i - dp[i]
    return " ".join(res)


def word_break2(str, word_dict):
    dp = [-1] * len(str)

    for i in range(len(str)):
        substr = str[:i+1]
        if substr in word_dict:
            dp[i] = i+1
            continue

        for j in range(i):
            if dp[j] != -1 and str[j+1: i+1] in word_dict:
                dp[i] = i - j
                break

    res = []
    i = len(str)-1
    if dp[-1] != -1:
        while i >= 0:

            res.append(str[i+1-dp[i]:i+1])
            i = i - dp[i]
    return " ".join(res)


def word_break_dp(str, word_dict):
    dp = [False] * (len(str)+1)
    dp[0] = True
    for i in range(len(str)):
        if dp[i]:
            for w in word_dict:
                if i + len(w) > len(str):
                    continue
                if str[i:i+len(w)] == w:
                    dp[i+len(w)] = True

    return dp[-1]


def word_break_rec(str, word_dict):

    def rec(str, i, word_dict):
        if i == len(str):
            return True

        for w in word_dict:
            if i + len(w) > len(str):
                continue
            if str[i:i+len(w)] == w:
                if rec(str, i+len(w), word_dict):
                    return True

        return False

    return rec(str, 0, word_dict)



if __name__ == "__main__":
    # print(minMeetingRooms([[1,8],[6,20],[9,16],[13,17]]))
    # print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    # print("Character order: " + find_order(["cab", "aaa", "aab"]))
    # print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
    # print(word_break2("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(word_break_rec("applepenapple", ["apple","pen"]))
