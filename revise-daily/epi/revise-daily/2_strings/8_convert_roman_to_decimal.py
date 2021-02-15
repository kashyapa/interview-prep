values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s):
    total = 0
    i = 0
    while i < len(s):
        # If this is the subtractive case.
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total += values[s[i + 1]] - values[s[i]]
            i += 2
        # Else this is NOT the subtractive case.
        else:
            total += values[s[i]]
            i += 1
    return total


def roman_to_int(s):
    sum = values[s[-1]]
    for i in reversed(range(len(s)-1)):
        if s[i] < s[i+1]:
            sum -= values[s[i]]
        else:
            sum += values[s[i]]
    return sum


if __name__ == '__main__':
    print(roman_to_int("XIX"))
