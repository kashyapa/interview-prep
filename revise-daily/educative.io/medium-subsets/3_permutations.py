# Given a set of distinct numbers, find all of its permutations.
#
# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
#
# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}
# If a set has ‘n’ distinct elements it will have n!n! permutations.

# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]


from collections import deque


def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])

    for i in range(len(nums)):
        for _ in range(len(permutations)):
            old_perm = permutations.popleft()

            for j in range(len(old_perm)+1):
                new_perm = list(old_perm)
                new_perm.insert(j, nums[i])
                if len(new_perm) == len(nums):
                    result.append(new_perm)
                else:
                    permutations.append(new_perm)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


if __name__ == "__main__":
    main()
