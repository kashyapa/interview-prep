from collections import deque


"""

    Iterate over the input array
    Iterate over the length of the permutation queue, for each item of input array
        
        for each permutation element, insert arr[i] at every index position in the permutation element
        
"""

def generate_permutations(arr):
    result = []
    permutations = deque()
    permutations.append([])

    for i in range(len(arr)):
        n = len(permutations)
        for _ in range(n):
            old_perm = permutations.popleft()
            for j in range(len(old_perm)+1):
                new_perm = list(old_perm)
                new_perm.insert(j, arr[i])
                if len(new_perm) == len(arr):
                    result.append(new_perm)
                else:
                    permutations.append(new_perm)

    return result


if __name__ == '__main__':
    arr = [2, 3, 5, 7]
    print(generate_permutations(arr))
