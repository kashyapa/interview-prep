def multiply(num1: list[int], num2: list[int]):

    sign = - 1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    res = [0] * len(len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i+j+1] += num1[i] * num2[j]
            res[i+j] = res[i+j+1] // 10
            res[i+j+1] %= 10

    # removing leading zeroes
    res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]