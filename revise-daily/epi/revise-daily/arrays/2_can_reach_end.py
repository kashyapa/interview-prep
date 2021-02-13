def can_reach_end(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1

    for i in range(len(arr)):
        if i > furthest_reach_so_far:
            return False
        furthest_reach_so_far = max(furthest_reach_so_far, i + arr[i])

    return True


if __name__ == "__main__":
    a = [2, 4, 1, 1, 0, 2, 3]
    res = can_reach_end(a)
    print(res)

    a = [3, 3, 1, 0, 2, 0, 1]
    res = can_reach_end(a)
    print(res)

    a = [3, 2, 0, 0, 2, 0, 1]
    res = can_reach_end(a)
    print(res)
