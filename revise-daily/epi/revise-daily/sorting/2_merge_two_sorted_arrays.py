def merge_two_sorted_arrays(A, B, m, n):

    i = m + n - 1

    a, b = m - 1, n-1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[i] = A[a]
            a -= 1
        else:
            A[i] = B[b]
            b -= 1

        i -= 1
    while b > 0:
        A[i] = B[b]
        b -= 1
        i -= 1
    return


if __name__ == '__main__':
    A = [3, 5, 6, 7, 0, 0, 0, 0, 0]
    B = [4, 5, 6, 7, 8]

    merge_two_sorted_arrays(A, B, 4, 5)

    print(A)