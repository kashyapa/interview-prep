import collections

def removeIslands(matrix):
    # Write your code here.
    queue = collections.deque()
    r = len(matrix)
    c = len(matrix[0])
    queue.extend(
        [(i, k) for i in range(r) for i, k in [(i, 0), (i, c - 1)] if matrix[i][k] == 1] +
        [(k, i) for i in range(c) for k, i in [(0, i), (r - 1, i)] if matrix[k][i] == 1]
    )

    while queue:
        i, j = queue.popleft()
        matrix[i][j] = -1
        for d1, d2 in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if matrix[i + d1][j + d2] == 1:
                queue.append((i + d1, j + d2))
    matrix = [0 for row in matrix for j in range(len(row)) if row[j] == 1]
    return matrix


def right_sibling_tree(root):
    # Write your code here.
    queue = collections.deque([root])
    head = root
    prev = None
    while queue:
        n = len(queue)
        for i in range(n):
            p = queue.popleft()
            if prev is not None:
                prev.right = p

            prev = p

            if i == n - 1:
                prev = None
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
    return head


from collections import deque

def subsets(nums):

    subsets = deque([])
    subsets.append([])

    for i in range(len(nums)):

        n = len(subsets)
        for j in range(n):
            p = subsets[j]
            new_subset = list(p)
            new_subset.append(nums[i])
            subsets.append(new_subset)
    return subsets


def subsets_with_duplicates(nums):
    subsets = []
    subsets.append([])
    start_index, end_index = 0, 0

    for i in range(len(nums)):
        start_index = 0
        if i >= 1 and nums[i] == nums[i-1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1

        for j in range(start_index, end_index+1):
            new_subset = list(subsets[j])
            new_subset.append(nums[i])
            subsets.append(new_subset)
    return subsets
#   abc
#   abc, Abc, aBc, ABc, abC, AbC, aBC, ABC
#
#
def permutations_by_swapping_case(str):

    perms = collections.deque([str])
    
    for i in range(len(str)):

        n = len(perms)
        for j in range(n):
            p = list(perms[j])
            p[i] = p[i].swapcase()
            perms.append(''.join(p))
    return perms



if __name__ == "__main__":
#     matrix = [
#   [1, 0, 0, 0, 0, 0],
#   [0, 1, 0, 1, 1, 1],
#   [0, 0, 1, 0, 1, 0],
#   [1, 1, 0, 0, 1, 0],
#   [1, 0, 1, 1, 0, 0],
#   [1, 0, 0, 0, 0, 1]
# ]
#     print(*removeIslands(matrix))
#     
#     
    tree = {
        "nodes": [
            {"id": "1", "left": "2", "right": "3", "value": 1},
            {"id": "3", "left": "6", "right": "7", "value": 3},
            {"id": "7", "left": "12", "right": "13", "value": 7},
            {"id": "13", "left": None, "right": None, "value": 13},
            {"id": "12", "left": None, "right": None, "value": 12},
            {"id": "6", "left": "11", "right": None, "value": 6},
            {"id": "11", "left": "14", "right": None, "value": 11},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "2", "left": "4", "right": "5", "value": 2},
            {"id": "5", "left": None, "right": "10", "value": 5},
            {"id": "10", "left": None, "right": None, "value": 10},
            {"id": "4", "left": "8", "right": "9", "value": 4},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "8", "left": None, "right": None, "value": 8}
        ],
        "root": "1" 
        }
    right_sibling_tree(tree)


