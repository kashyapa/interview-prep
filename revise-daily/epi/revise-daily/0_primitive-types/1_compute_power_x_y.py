def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x

    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1

    return result

def compute_power2(x, y):
    if y < 0:
        x = 1.0 / x
        y = -y

    if y == 1:
        return x
    if y == 0:
        return 1

    if y % 2 == 1:
        return x * compute_power2(x, y//2) * compute_power2(x, y//2)

    return compute_power2(x, y//2) * compute_power2(x, y//2)


if __name__ == "__main__":
    print(power(2, 3))
    print(power(2, -3))
    print(compute_power2(2, 3))
    print(compute_power2(2, -3))