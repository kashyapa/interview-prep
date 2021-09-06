from collections import deque

def minimum_passes_of_matrix(matrix):

    def is_convertible(i, j):

        if i+1 < len(matrix) and matrix[i+1][j] > 0:
            return True
        if i-1 >= 0 and matrix[i-1][j] > 0:
            return True
        if j-1 >= 0 and matrix[i][j-1] > 0:
            return True
        if j+1 < len(matrix[0]) and matrix[i][j+1] > 0:
            return True
        return False


    queue = deque([])
    negatives = set()
    converted = set()
    count = 0

    while True:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    negatives.add(str(i)+"-"+str(j))
                    if is_convertible(i, j):
                        converted.add(str(i)+"-"+str(j))
                        queue.append((i, j))

        if queue:
            count += 1
            while queue:
                i, j = queue.popleft()
                matrix[i][j] = -1 * matrix[i][j]

        else:
            break
    return count  if len(converted) == len(negatives) else -1
