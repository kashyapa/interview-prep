import collections

def nextGreaterElement(array):
    # Write your code here.
    queue = []

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            queue.append((array[i], i))
    res = [-1] * len(array)
    l = 0
    copy_list = queue[:]
    queue.extend(copy_list)
    while queue:
        val, idx = queue.pop(0)
        j = idx - 1
        while array[j] < val and res[j] == -1:
            res[j] = val
            j -= 1
        l = idx
    return res

def nextGreaterElement2(array):
    # Write your code here.
    stack = array[::-1]
    res = [-1] * len(array)
    for i in reversed(range(len(array))):
        while stack and stack[-1] <= array[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(array[i])
    return res


if __name__ == "__main__":
    print(nextGreaterElement2([6, 4, 5, 7, 2, 1, 3]))