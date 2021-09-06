from heapq import *
import collections

def word_break(long_word, word_list):
    
    def rec(word):
        if len(word) == 0:
            return True

        for w in word_list:
            if word.startswith(w) and rec(word[len(w):]):
                return True
        
        return False
    return rec(long_word)


class BuildingData:
    def __init__(self, point, height, is_end=False):
        self.point = point
        self.height = height
        self.is_end = is_end

    def __lt__(self, other):
        return self.height - other.height


def get_skyline(building_info):

    start_points = [BuildingData(b[0], b[2]) for b in building_info]
    end_points = [BuildingData(b[1], b[2], True) for b in building_info]

    max_heap = [0]

    building_points = start_points + end_points

    building_points.sort(key=lambda x: x.point)

    res = []
    for b in building_points:
        if not b.is_end:
            if not max_heap or b.height > max_heap[0]:
                res.append((b.point, b.height))
            heappush(max_heap,  b.height)
        else:
            max_heap.remove(b.height)
            heapify(max_heap)
            if max_heap[0] < b.height:
                res.append((b.point, b.height))
    return res


def regular_expressions(str, pattern):
    def rec(str, pattern):

        if pattern == "$":
            return not str

        if not str:
            return True

        if len(pattern) >= 2 and pattern[0] == "*":
                i = 1
                while i <= len(str) and pattern[0] in (str[i-1], "."):
                    if rec(str[i:], pattern[2:]):
                        return True
                    i += 1
                return rec(str, pattern[2:])
        return pattern[0] in (str[0], ".") and rec(str[1:], pattern[1:])

    if pattern[0] == "^":
        return rec(str, pattern[1:])
    return rec(str, pattern)


def maximal_square(matrix):
    dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
    max_square = 0
    for i in range(1, len(matrix)+1):
        for j in range(1, len(matrix[0])+1):
            if matrix[i-1][j-1] == "1":
                dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
                max_square = max(max_square, dp[i][j])

    return max_square * max_square


def maximal_rectangle(matrix):

    def largest_cumulative_area(row):
        pillars = []
        max_area = 0
        for i, n in enumerate(row+[0]):
            while pillars and n <= row[pillars[-1]]:
                height = row[pillars.pop()]
                width = i if not pillars else i - pillars[-1] - 1
                max_area = max(max_area, width * height)
            pillars.append(i)
        return max_area

    max_rectangle = 0
    table = [0] * len(matrix[0])
    for row in matrix:
        row = list(map(int, [y for x in row for y in x]))

        table = [x+y if y else 0 for x,y in zip(table, row)]
        max_rectangle = max(max_rectangle, largest_cumulative_area(table))
    return max_rectangle


class LRUCache:

    def __init__(self, capacity):
        self.queue = collections.deque()
        self.map = {}
        self.capacity = capacity


    def get(self, key):
        if key in self.map:
            self.queue.remove(key)
            self.queue.append(key)
            return self.map[key]
        return None

    def put(self, key, value):
        if self.capacity == len(self.map):
            k = self.queue.popleft()
            del self.map[k]

        if key in self.map:
            self.queue.remove(key)
        self.map[key] = value
        self.queue.append(key)


def longest_valid_parentheses(parentheses):

    stack = []
    max_length = 0
    start, end = -1, -1
    for i in range(len(parentheses)):
        if parentheses[i] == "(":
            stack.append(i)
        elif not stack:
            start = i
        else:
            stack.pop()
            length = i - start + 1 if not stack else i - stack[-1] + 1
            max_length = max(max_length, length)

    return max_length



def longest_valid_subarray_sum(nums, k):
    count = collections.defaultdict(int)

    for i in range(len(nums)):
        sum += nums[i]
        if sum-k in map:
            count += map[sum]+1
        map[sum] = map[sum]+1
    return count


def compute_salary_thresholds(salaries, target):

    salaries.sort()
    threshold = 0
    cumulative_salary = 0
    for i in range(len(salaries)):
        cumulative_salary += salaries[i]
        remaining_sum = target - cumulative_salary
        threshold = remaining_sum // (len(salaries) - i)


def edit_distance(s1, s2):
    def rec(s1, s2, i1, i2):
        if i1 == 0:
            return i2+1
        elif i2 == 0:
            return i1+1

        if s1[i1] == s2[i2]:
            return rec(s1, s2, i1-1, i2-1)

        replace_character = rec(s1, s2, i1-1, i2-1)
        add_character = rec(s1, s2, i1-1, i2)
        delete_character = rec(s1, s2, i1, i2 -1)
        
        return 1+min(replace_character, add_character, delete_character)

    return rec(s1, s2, len(s1)-1, len(s2)-1)


def is_substring_concatenation_of_words(s, words_set):
    unit_size = len(words_set[0])
    res = []
    for i in range(len(s)):
        substr = s[i:i+unit_size]
        if substr in words_set:
            j = i
            word_count = collections.Counter(words_set)
            remaining_words = len(words_set)

            while True:
                substr = s[j:j+unit_size]
                if word_count[substr] > 0:
                    remaining_words -= 1
                    word_count[substr] -= 1
                else:
                    break
                if remaining_words == 0:
                    res.append(i)
                j += unit_size
    return res


def bed_bath_beyond(s, word_collection):

    dp = [-1] * (len(s)+1)

    for i in range(1, len(s)):
        prefix = s[:i+1]
        if prefix in word_collection:
            dp[i] = i+1
            continue
        for j in range(i):
            print(len(s), ": ", j)
            if dp[j] != -1:
                substr = s[j+1:i+1]
                if substr in word_collection:
                    dp[i] = i - j
                    break
    res = []
    i = len(s)-1
    while i >= 0:
        res.append(s[i-dp[i]+1:i+1])
        print(s[i-dp[i]+1:i+1])
        i -= dp[i]
    return res


def word_pattern(s, pattern):

    def rec_backtrack(s, start_idx, pattern_idx):

        if pattern_idx == len(pattern):
            return start_idx == len(s)
        elif pattern_idx == len(pattern) or start_idx == len(s):
            return False

        p = pattern[pattern_idx]
        if p in pattern_map:
            matching_str = pattern_map[p]
            if s.startswith(matching_str, start_idx):
                return rec_backtrack(s, start_idx+len(matching_str), pattern_idx+1)

        for j in range(start_idx, len(s)):
            substr = s[start_idx:j+1]
            if substr in matched_str:
                continue
            pattern_map[p] = substr
            if rec_backtrack(s, start_idx+len(substr), pattern_idx+1):
                return True
            del pattern_map[p]
            matched_str.remove(substr)

        return False
    matched_str = set()
    pattern_map = {}
    return rec_backtrack(s, 0, 0)


import string
def word_ladder(s1, s2, words_set: set):

    queue = collections.deque([(s1, 0)])
    words_set.remove(s1)

    while queue:
        s, distance = queue.popleft()
        if s == s2:
            return distance
        for i in range(len(s)):
            for c in string.ascii_lowercase:
                next_word = s[:i]+c+s[i+1:]
                if next_word in words_set:
                    queue.append((next_word, distance+1))
                    words_set.remove(next_word)

    return -1

# def compute_valid_ip_addresses(s):
#
#     def is_valid_part(str):
#         return len(str) == 1 or (str[0]!=255 and int(str) <= 255)
#
#     parts = [""] * 4
#     for i in range(len(s)-3):
#         parts[0] = s[:i+1]
#         if is_valid_part
#         for j in range(1, min(len(s)-i, 4)):
#             parts[1] = s[i:i+j]

# Python3 code to check valid possible IP

# Function checks whether IP digits
# are valid or not.
def is_valid(ip):
    # Splitting by "."
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
            int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
            i[0] == '0'):
            return False

    return True


# Function converts string to IP address
def convert(s):
    sz = len(s)

    # Check for string size
    if sz > 12:
        return []
    snew = s
    l = []

    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)

                snew = s

    return l



def convert_roman_to_decimal(s):
    map  = {
        "I": 1,
        "V": 5,
        "X": 10
    }
    n = map[s[-1]]
    for i in reversed(range(len(s)-1)):
        if map[s[i]] < map[s[i+1]]:
            n -= map[s[i]]
        else:
            n += map[s[i]]
    return n

import math
def find_largest_two_numbers(arr):
    largest, second_largest = -math.inf, -math.inf

    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest:
            second_largest = arr[i]
    return largest, second_largest


def sort_arrays_of_1s_and_0s(arr):
    res = [0] * len(arr)
    ones_count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            ones_count += 1
    for i in range(ones_count):
        res[i] = 1
    return res


def sort_arrays_of_ones_and_zeros(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    return arr

# solution 1
# sort nums
def find_duplicate_number_within_range(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

#solution 2
def find_duplicates_using_a_set(nums):
    unique_elems = set()
    for i in range(len(nums)):
        if nums[i] in unique_elems:
            return nums[i]
        unique_elems.add(nums[i])

# solution 3
def find_duplicates_using_boolean_array(nums):
    exists = [False] * len(nums)

    for i in range(len(nums)):
        if exists[nums[i]-1]:
            return nums[i]
        exists[nums[i]-1] = True
# solution 4        
def find_duplicates_using_in_place_swap(nums):
    i = 0
    while i < len(nums):
        actual_index = nums[i]-1
        if nums[i] != nums[actual_index]:
            nums[i], nums[actual_index] = nums[actual_index], nums[i]
        else:
            i += 1
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]
    return -1

class Tree:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

class Diameter:
    def __init__(self):
        self.diameter = 0

    def diameter_of_tree(self, root: Tree):

        def find_height(node: Tree):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return 1

            lh = find_height(node.left)
            rh = find_height(node.right)

            self.diameter = max(self.diameter, lh+rh+1)
            return 1 + max(lh, rh)


        find_height(root)
        return self.diameter

def max_path_sum(root: Tree):

    def rec(node):

        if node is None:
            return 0

        elif node.left is None and node.right is None:
            return node.val

        lsum = rec(node.left)
        rsum = rec(node.right)
        max_sum[0] = max(max_sum[0], max(lsum+node.val+rsum, max(lsum+node.val, rsum+node.val)))
        return node.val + max(lsum, rsum)

    rec(root)
    max_sum = (-math.inf)



def root_to_leaf_path_sum(root: Tree, target):
    def rec(node: Tree, remaining_sum, path):

        if node is None:
            if remaining_sum == 0:
                all_paths.append(path.copy())
                return
        path.append(node.val)
        # remaining_sum -= node.val
        rec(node.left, remaining_sum-node.val, path)
        rec(node.right, remaining_sum-node.val, path)
        path.pop()
        return

    all_paths = []
    return rec(root, target, [])

def reverse_words(sentence):

    def reverse(i, j):
        while i < j:
            word_list[i], word_list[j] = word_list[j], word_list[i]
            i += 1
            j -= 1
        return

    word_list = list(sentence)

    i, j= 0, 0
    reverse(0, len(word_list)-1)

    while j < len(word_list):
        while j < len(word_list) and word_list[j] == " ":
            j += 1
        if j == len(word_list):
            break
        i = j
        while j < len(word_list) and word_list[j] != " ":
            j += 1

        if j == len(word_list):
            break

        reverse(i, j-1)
    reverse(i, len(word_list)-1)
    return "".join(word_list)



def median_of_two_sorted_arrays(nums1, nums2):
    i1, i2 = 0, 0
    n1, n2 = len(nums1), len(nums2)
    total_len = (n1+n2)//2

    prev, cur = 0, 0
    i = 0
    while i <= total_len // 2:
        prev = cur
        if i1 == n1:
            cur = nums2[i2]
        elif i2 == n2:
            cur = nums1[i1]
        if nums1[i1] < nums2[i2]:
            cur = nums1[i1]
            i1 += 1
        else:
            cur = nums2[i2]
            i2 += 1

        i += 1
    if total_len % 2 == 0:
        return (prev + cur) // 2
    return cur

#
# def median_binary_search(nums1, nums2)
#
#     x = len(nums1)
#     y = len(nums2)
#
#     lo , hi = 0, x
#     while lo <= hi:
#         partition_x = (lo+hi) // 2
#         partition_y = (x+y+1) // 2 - partition_x
#
#         max_left_x =  -math.inf  if partition_x == 0 else nums1[partition_x-1]
#         min_right_x = math.inf if partition_x == x else nums1[partition_x]
#
#         max_left_Y = -math.inf if partition_y == 0 else nums2[partition_y -1]
#         min_right_y = math.inf if partition_y == y else nums2[partition_y]
#
#         if max_left_x < min_right_y and max_left_Y < min_right_x:
#             if (x+y)%2 == 0:
#                 return (max(max_left_x, max_left_Y) + min(min_right_y, min_right_x)) // 2
#             return max(max_left_x, max_left_Y)
#         elif max_left_x > min_right_y:
#             hi = partition_x - 1
#         else:
#             lo = partition_x + 1

from heapq import *

class MedianOfStream:

    max_heap = []
    min_heap = []

    def insert_num(self, num):

        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            p = -heappop(self.max_heap)
            heappush(self.min_heap, p)
        elif len(self.max_heap)+1 < len(self.min_heap):
            p = heappop(self.min_heap)
            heappush(self.max_heap, -p)

import random
def kth_largest_element(nums, k):

    def partition(nums, l, r, pivot_idx):
        pivot = nums[pivot_idx]

        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        less_than_pivot = l
        for i in range(l, r):
            if nums[i] > pivot:
                nums[i],nums[less_than_pivot] = nums[less_than_pivot], nums[i]
                less_than_pivot += 1

        nums[less_than_pivot], nums[r] = nums[r], nums[less_than_pivot]
        return less_than_pivot

    l, r = 0, len(nums)-1

    while l < r:
        pivot_idx = random.randint(l, r)
        pivot_idx = partition(nums, l, r, pivot_idx)
        if pivot_idx == k - 1:
            return nums[pivot_idx]
        elif pivot_idx > k - 1:
            r = pivot_idx - 1
        else:
            l = pivot_idx + 1
    return -1

def merge_sort(nums):

    def merge(A, B):
        res = []
        i, j = 0 , 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        res.extend(A[i:])
        res.extend(B[j:])

        return res

    if len(nums) == 1:
        return nums
    l, r = 0, len(nums) -1
    mid = (l+r)//2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge_k_sorted_lists(lists):
    def merge(A, B):
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        res.extend(A[i:])
        res.extend(B[j:])

        return res
    if len(lists) == 1:
        return lists
    l, r = 0, len(lists) - 1
    intermediate_list = []
    while l < r:
        res = merge(lists[l], lists[r])
        intermediate_list.append(res)
        r -= 1
        l += 1
    res2 = merge_k_sorted_lists(intermediate_list)
    return res2

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

def next_interval(intervals):
    max_start_heap = []
    max_end_heap = []

    for i in range(len(intervals)):
        heappush(max_start_heap, (-intervals[i].start, i))
        heappush(max_end_heap, (-intervals[i].end, i))

    res = [0 for _ in range(len(intervals))]

    for _ in range(len(intervals)):
        max_end, end_idx = heappop(max_end_heap)
        res[end_idx] = -1

        if -max_start_heap[0][0] > max_end:
            start_point, start_idx = heappop(max_start_heap)
            while max_start_heap and -max_start_heap[0][0] > max_end:
                start_point, start_idx = heappop(max_start_heap)
            res[end_idx] = start_idx
            heappush(max_start_heap, (start_point, start_idx))
    return res


def find_maximum_capital(capitals, profits, number_of_projects, initial_capital):
    max_heap = []
    min_heap = []

    for i in range(number_of_projects):
        heappush(min_heap, (capitals[i], i))

    available_capital = initial_capital

    for _ in range(number_of_projects):

        while min_heap[0][0] <= available_capital:
            capital, i = heappop(min_heap)
            heappush(max_heap, -profits[i])

        available_capital += -heappop(max_heap)
    return available_capital


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        levels = {-1: 0}

        max_len = 0
        for token in input.split("\n"):
            level = token.count("\t")

            levels[level] = levels[level - 1] + len(token) - level

            if "." in token:
                max_len = max(max_len, levels[level] + level)
        return max_len


def coinChange(coins, amount):
    def rec(idx, remaining_amt):

        if remaining_amt == 0:
            return 0
        if idx == len(coins):
            return -1
        with_cur_coin = len(coins)
        if coins[idx] <= remaining_amt:
            res = rec(idx, remaining_amt - coins[idx])
            if res != -1:
                with_cur_coin = 1 + res

        without_cur_coin = rec(idx + 1, remaining_amt)
        return max(with_cur_coin, without_cur_coin)

    coins.sort(reverse=True)
    return rec(0, amount)


if __name__ == "__main__":
    # print(word_break("leetcode", ["leet", "code"]))
    # print(get_skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    # print(maximal_square([["1","0","1","0","0"],
    #                      ["1","0","1","1","1"],
    #                      ["1","1","1","1","1"],
    #                      ["1","0","1","1","1"]]))
    #
    # print(maximal_rectangle([["1","0","1","0","0"],
    #                         ["1","0","1","1","1"],
    #                         ["1","1","1","1","1"],
    #                         ["1","0","0","1","0"]]))
    #
    # cache = LRUCache(2)
    # cache.put(1, 4)
    # cache.put(2, 5)
    # print(cache.get(1)) #returns 4
    # print(cache.get(5)) # returns -1
    # print(cache.put(3, 6)) # removes key 2
    # print(cache.get(2)) # retruns -1
    #
    # print(is_substring_concatenation_of_words("amanaplanacanal", ["ana", "pla"]))
    # print(is_substring_concatenation_of_words("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    # print(is_substring_concatenation_of_words("catfoxcat", ["cat", "fox"]))
    # print(is_substring_concatenation_of_words("barfoothefoobarman",["foo", "bar"]))
    # print(is_substring_concatenation_of_words("barfoofoobarthefoobarman", ["bar","foo","the"]))
    #
    # set2 = {"bed", "bath", "bat", "beyond", "hand", "and"}
    # print(bed_bath_beyond("bedbathandbeyond", set2))
    #
    # # Driver code
    # A = "25525511135"
    # B = "25505011535"
    #
    # print(convert(A))
    # print(convert(B))
    # convert_roman_to_decimal("IVXCDM")

    print("**** find duplicates  ******")
    print(find_duplicates_using_in_place_swap([1, 4, 4, 3, 2]))
    print(find_duplicates_using_boolean_array([2, 1, 3, 3, 5, 4]))
    print(find_duplicates_using_a_set([2, 4, 1, 4, 4]))
    print(find_duplicate_number_within_range([2, 4, 1, 4, 4]))

    bits = [1, 1, 0, 1]
    print(sort_arrays_of_1s_and_0s(bits))
    print(sort_arrays_of_ones_and_zeros(bits))

    numbers = [12,3,15,92]
    print(find_largest_two_numbers(numbers))

    print(reverse_words("this is a sentence,         reverse the order of the words"))

    print(median_of_two_sorted_arrays([1, 2], [3,4]))

    print(coinChange([1,2,5], 11))