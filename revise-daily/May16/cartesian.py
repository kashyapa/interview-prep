from typing import List


# Problem:

# Please implement a function cartesian that produces the cartesian product of a list with itself k times.

def cartesian(input_list: List[str], k: int) -> List[List[str]]:
    if k == 1:
        return [[input_list[i]] for i in range(len(input_list))]
    result = []

    for i in range(k):
        res = cartesian(input_list, k - 1)
        for t in res:
            for j in input_list:
                result.append([*t, j])
    return result


assert cartesian(['a', 'b', 'c'], 1) == [['a'], ['b'], ['c']]
assert cartesian(['a', 'b', 'c'], 2) == [['a', 'a'], ['a', 'b'], ['a', 'c'],
                                         ['b', 'a'], ['b', 'b'], ['b', 'c'],
                                         ['c', 'a'], ['c', 'b'], ['c', 'c']]

# print(cartesian(['a', 'b', 'c'], 3))