import bisect

# if length of arr1 and arr2 are very different


def compute_intersection(arr1, arr2):

    def is_present(k):
        i = bisect.bisect_left(arr2, k)
        return i < len(arr2) and arr2[i] == k

    return [
        a for i, a in enumerate(arr1)
        if i == 0 and a != arr1[i-1] and is_present(a)
    ]


# if len A and len B are similar
def compute_intersection_a_b(A, B):

    i, j = 0, 0
    intersection = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        else:
            if A[i] > B[j]:
                j += 1
            else:
                i += 1

    return intersection
