


def threeNumberSum(array, targetSum):
    # Write your code here.
    def two_pair_sum(array, i, target):

        l,j = i+1, len(array) - 1
        while l < j:
            if array[l] + array[j] == target:
                res.append([array[i], array[l],  array[j]])
                l += 1
                j -= 1
            elif j == len(array) - 1 or array[j] == array[j+1] or array[l] + array[j] > target:
                j -= 1
            elif array[l] == array[l-1] or array[l]+array[j] < target:
                l += 1
        return

    res = []
    array.sort()

    for i in range(len(array) - 2):
        if i == 0 or array[i] != array[i-1]:
            two_pair_sum(array, i, targetSum - array[i])

    return res


if __name__ == "__main__":
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))