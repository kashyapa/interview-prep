def fourNumberSum(array, targetSum):
    # Write your code here.

    def find_two_sum(sum, second, first):
        third = second + 1
        fourth = len(array) - 1
        while third < fourth:
            while third < fourth and array[third] == array[third - 1]:
                third += 1
            while fourth < len(array) - 1 and fourth > third and array[fourth] == array[fourth + 1]:
                fourth -= 1
            if array[third] + array[fourth] > sum:
                fourth -= 1
            elif array[third] + array[fourth] < sum:
                third += 1
            else:
                res.append([array[first], array[second], array[third], array[fourth]])
                third+=1
                fourth-=1

    def find_three_sum(target, first):
        for l in range(first + 1, len(array) - 2):
            if array[l] != array[l - 1]:
                find_two_sum(target - array[l] - array[first], l, first)

    array.sort()

    res = []
    for i in range(len(array) - 3):
        if i == 0 or array[i] != array[i - 1]:
            find_three_sum(targetSum, i)
    return res


if __name__=="__main__":
    print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))