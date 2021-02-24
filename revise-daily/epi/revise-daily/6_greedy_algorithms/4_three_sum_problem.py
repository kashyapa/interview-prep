def three_sum_problem(arr: list, target: int):

    def two_sum(arr, sum):
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] + arr[j] == sum:
                return True
            if arr[i] < arr[j]:
                i += 1
            else:
                j -= 1
        return False
    arr.sort()
    return any(
        two_sum(arr, target-a) for a in arr
    )
